import os
import re
import sqlite3
import numpy as np
import base64
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file
import io
import csv

# Safe import for OpenCV (cv2)
try:
    import cv2
    CV2_AVAILABLE = True
    print("[INFO] OpenCV (cv2) loaded successfully.")
except ImportError:
    cv2 = None
    CV2_AVAILABLE = False
    print("[NOTICE] OpenCV (cv2) is not installed. Run 'pip install opencv-python' in your terminal.")

# Initialize Flask app
app = Flask(__name__, template_folder="templates")

# In serverless environments like Vercel, the root filesystem is read-only except /tmp
if os.environ.get("VERCEL"):
    DB_NAME = "/tmp/attendance.db"
    if not os.path.exists(DB_NAME) and os.path.exists("attendance.db"):
        try:
            import shutil
            shutil.copy2("attendance.db", DB_NAME)
        except Exception:
            pass
else:
    DB_NAME = "attendance.db"

# Optional: Try to import EasyOCR if installed; provide high-speed fallback
try:
    import easyocr
    ocr_reader = easyocr.Reader(['en'], gpu=False)
    OCR_AVAILABLE = True
    print("[INFO] EasyOCR loaded successfully.")
except Exception as e:
    ocr_reader = None
    OCR_AVAILABLE = False
    print("[NOTICE] EasyOCR not installed or initializing; using heuristic pattern fallback.")

# ==========================================
# DATABASE HELPER FUNCTIONS
# ==========================================
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll_number TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            year TEXT NOT NULL,
            section TEXT NOT NULL
        )
    """)

    # Attendance logs table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_number TEXT NOT NULL,
            student_name TEXT,
            department TEXT,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            status TEXT NOT NULL,
            method TEXT NOT NULL,
            UNIQUE(roll_number, date)
        )
    """)
    conn.commit()

    # Pre-populate sample students including the candidate
    sample_students = [
        ("2403A52218", "Padhy Aarnav", "BTech - CSE - AIML", "2024-2028", "Section A"),
        ("2403A52423", "Vydha Snehal Shiva Sai", "BTech - CSE - AIML", "2024-2028", "Section A"),
        ("2303A58033", "Aadithiya Binu Antony", "B.Tech - CSE (CSIEP)", "2023-2027", "Section A"),
        ("2402A71066", "Md Fardeen Ahmed Amaan", "BBA - BM", "2024-2027", "Section A"),
        ("2403A51409", "Student 2403A51409", "BTech - CSE - AIML", "2024-2028", "Section A"),
        ("2403A62218", "Padhy Aarnav", "BTech - CSE - AIML", "2024-2028", "Section A"),
        ("2403A54001", "Aarav Sharma", "BTech - CSE - AIML", "2024-2028", "Section A"),
        ("2403A54012", "Bhavya Reddy", "BTech - CSE - AIML", "2024-2028", "Section A"),
        ("2403A54020", "Chirag Patel", "BTech - CSE - AIML", "2024-2028", "Section B"),
        ("2403A54044", "Divya Teja", "BTech - CSE - AIML", "2024-2028", "Section A"),
        ("2403A54055", "Eshwar Varma", "BTech - CSE - AIML", "2024-2028", "Section B")
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO students (roll_number, name, department, year, section)
        VALUES (?, ?, ?, ?, ?)
    """, sample_students)
    conn.commit()
    conn.close()

# ==========================================
# IMAGE PROCESSING & RECTIFICATION
# ==========================================
def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect

def four_point_transform(image, pts):
    if not CV2_AVAILABLE or cv2 is None or image is None:
        return image
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    width_a = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    width_b = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    computed_w = max(int(width_a), int(width_b))

    height_a = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    height_b = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    computed_h = max(int(height_a), int(height_b))

    # Detect orientation: if height >= width (Portrait ID card like SRU ID), maintain portrait aspect ratio
    if computed_h >= computed_w:
        max_w = max(computed_w, 480)
        max_h = int(max_w * 1.58)  # Standard Portrait CR-80 card ratio
    else:
        max_w = max(computed_w, 480)
        max_h = int(max_w * 0.63)  # Standard Landscape CR-80 card ratio

    dst = np.array([
        [0, 0],
        [max_w - 1, 0],
        [max_w - 1, max_h - 1],
        [0, max_h - 1]
    ], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    return cv2.warpPerspective(image, M, (max_w, max_h))

def find_card_bounding_polygon(cv_img):
    if not CV2_AVAILABLE or cv2 is None or cv_img is None:
        return None
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]
    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4 and cv2.contourArea(c) > 20000:
            return approx.reshape(4, 2)
    return None

@app.after_request
def add_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
    return response

# ==========================================
# ROUTES & REST APIS
# ==========================================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/stats")
def get_stats():
    conn = get_db_connection()
    today = datetime.now().strftime("%Y-%m-%d")
    
    total_students = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    present_today = conn.execute("SELECT COUNT(*) FROM attendance WHERE date = ?", (today,)).fetchone()[0]
    
    attendance_rate = round((present_today / total_students * 100), 1) if total_students > 0 else 0
    
    conn.close()
    return jsonify({
        "total_students": total_students,
        "present_today": present_today,
        "absent_today": max(0, total_students - present_today),
        "attendance_rate": attendance_rate,
        "date": today
    })

@app.route("/api/attendance", methods=["GET"])
def get_attendance():
    conn = get_db_connection()
    today = datetime.now().strftime("%Y-%m-%d")
    logs = conn.execute("""
        SELECT a.id, a.roll_number, IFNULL(s.name, a.student_name) as name, 
               IFNULL(s.department, a.department) as department, 
               a.date, a.time, a.status, a.method
        FROM attendance a
        LEFT JOIN students s ON a.roll_number = s.roll_number
        WHERE a.date = ?
        ORDER BY a.id DESC
    """, (today,)).fetchall()
    
    conn.close()
    return jsonify([dict(row) for row in logs])

@app.route("/api/clear", methods=["POST", "GET"])
def clear_attendance():
    conn = get_db_connection()
    conn.execute("DELETE FROM attendance")
    conn.commit()
    conn.close()
    return jsonify({"success": True, "message": "All attendance records cleared successfully."})

@app.route("/api/students", methods=["GET"])
def get_students():
    conn = get_db_connection()
    students = conn.execute("SELECT * FROM students ORDER BY roll_number ASC").fetchall()
    conn.close()
    return jsonify([dict(row) for row in students])

@app.route("/api/students/update", methods=["POST"])
def update_student():
    data = request.json or {}
    roll = data.get("roll_number")
    name = data.get("name")
    if not roll or not name:
        return jsonify({"success": False, "message": "Roll and Name required."}), 400
    conn = get_db_connection()
    conn.execute("UPDATE students SET name = ? WHERE roll_number = ?", (name, roll))
    conn.execute("UPDATE attendance SET student_name = ? WHERE roll_number = ?", (name, roll))
    conn.commit()
    conn.close()
    return jsonify({"success": True, "message": f"Updated {roll} to {name}"})

@app.route("/api/scan", methods=["POST"])
def scan_id_card():
    data = request.json
    if not data or "image" not in data:
        return jsonify({"success": False, "message": "No image payload received."}), 400

    image_b64 = data["image"].split(",")[-1]
    image_bytes = base64.b64decode(image_b64)
    np_arr = np.frombuffer(image_bytes, np.uint8)
    frame = None
    if CV2_AVAILABLE and cv2 is not None:
        try:
            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        except Exception:
            frame = None

    # Perspective rectification
    card_contour = find_card_bounding_polygon(frame) if frame is not None else None
    if card_contour is not None and frame is not None:
        processed_card = four_point_transform(frame, card_contour)
    else:
        processed_card = frame

    detected_text = ""
    extracted_roll = None

    # Run OCR if EasyOCR is loaded and frame is available
    if OCR_AVAILABLE and ocr_reader and processed_card is not None and CV2_AVAILABLE:
        try:
            gray_card = cv2.cvtColor(processed_card, cv2.COLOR_BGR2GRAY)
            # Run OCR on full card to cover both front (bottom half) and back (top half)
            results = ocr_reader.readtext(gray_card, detail=0)
            detected_text = " ".join(results).upper().replace(" ", "").replace("O", "0")
        except Exception as e:
            print("[ERROR in OCR]:", e)

    # Universal Roll number regex pattern (e.g. 2403A52423, 2303A58033, 2402A71066, etc.)
    pattern = re.compile(r'(?:2[0-6]\d{2}[A-Z][0-9A-Z]{5,6})', re.IGNORECASE)
    matches = pattern.findall(detected_text)
    if matches:
        extracted_roll = matches[0].upper()
    
    # Optional client-provided roll fallback (for browser-side OCR / direct input)
    if not extracted_roll and "manual_roll" in data and data["manual_roll"]:
        extracted_roll = data["manual_roll"].strip().upper()

    if not extracted_roll:
        return jsonify({
            "success": False, 
            "card_detected": card_contour is not None,
            "message": "Roll Number not cleanly recognized. Please hold card steady inside the box or click upload."
        })

    # Record attendance in database
    conn = get_db_connection()
    today = datetime.now().strftime("%Y-%m-%d")
    now_time = datetime.now().strftime("%H:%M:%S")

    # Look up student in registry or auto-enroll
    student = conn.execute("SELECT * FROM students WHERE roll_number = ?", (extracted_roll,)).fetchone()
    incoming_name = data.get("student_name")
    
    if student:
        student_name = student["name"]
        department = student["department"]
        # If student exists but had a placeholder name, upgrade it if a real name was provided
        if incoming_name and (student_name.startswith("Student ") or student_name == "Unknown Student"):
            conn.execute("UPDATE students SET name = ? WHERE roll_number = ?", (incoming_name, extracted_roll))
            conn.execute("UPDATE attendance SET student_name = ? WHERE roll_number = ?", (incoming_name, extracted_roll))
            conn.commit()
            student_name = incoming_name
    else:
        # Auto-enroll student into registry with their real name
        KNOWN_STUDENT_NAMES = {
            "2403A52218": "Padhy Aarnav",
            "2403A62218": "Padhy Aarnav",
            "2403A52423": "Vydha Snehal Shiva Sai",
            "2303A58033": "Aadithiya Binu Antony",
            "2402A71066": "Md Fardeen Ahmed Amaan",
            "2403A51409": "Student 2403A51409"
        }
        student_name = incoming_name or KNOWN_STUDENT_NAMES.get(extracted_roll, f"Student {extracted_roll}")
        department = data.get("department") or "BTech - CSE - AIML"
        conn.execute("""
            INSERT OR REPLACE INTO students (roll_number, name, department, year, section)
            VALUES (?, ?, ?, ?, ?)
        """, (extracted_roll, student_name, department, "2024-2028", "Section A"))
        conn.commit()

    # Check for existing check-in today
    existing = conn.execute("SELECT * FROM attendance WHERE roll_number = ? AND date = ?", 
                            (extracted_roll, today)).fetchone()

    if existing:
        conn.close()
        return jsonify({
            "success": False,
            "roll_number": extracted_roll,
            "name": student_name,
            "message": f"Attendance already logged today at {existing['time']}."
        })

    # Insert log
    conn.execute("""
        INSERT INTO attendance (roll_number, student_name, department, date, time, status, method)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (extracted_roll, student_name, department, today, now_time, "PRESENT", "DL-ID-Scan"))
    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "roll_number": extracted_roll,
        "name": student_name,
        "department": department,
        "time": now_time,
        "message": f"Verified! Attendance marked for {student_name} ({extracted_roll})."
    })

@app.route("/api/export")
def export_csv():
    conn = get_db_connection()
    today = datetime.now().strftime("%Y-%m-%d")
    logs = conn.execute("""
        SELECT a.roll_number, IFNULL(s.name, a.student_name) as name, 
               IFNULL(s.department, a.department) as department, 
               a.date, a.time, a.status, a.method
        FROM attendance a
        LEFT JOIN students s ON a.roll_number = s.roll_number
        WHERE a.date = ?
        ORDER BY a.id ASC
    """, (today,)).fetchall()
    conn.close()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Roll Number", "Student Name", "Department", "Date", "Time", "Status", "Verification Method"])
    for row in logs:
        writer.writerow([row["roll_number"], row["name"], row["department"], row["date"], row["time"], row["status"], row["method"]])
    
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype="text/csv",
        as_attachment=True,
        download_name=f"Attendance_Report_{today}.csv"
    )

import socket

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

@app.route("/api/network-info")
def network_info():
    ip = get_local_ip()
    return jsonify({
        "local_ip": ip,
        "mobile_url": f"http://{ip}:5000"
    })

if __name__ == "__main__":
    init_db()
    local_ip = get_local_ip()
    print("\n=======================================================")
    print("SRU Smart Attendance Management System - DL ID Card")
    print("Local URL:    http://127.0.0.1:5000")
    print(f"📱 iPhone URL: http://{local_ip}:5000 (Open in Safari on iPhone)")
    print("=======================================================\n")
    app.run(debug=False, host="0.0.0.0", port=5000, threaded=True)
