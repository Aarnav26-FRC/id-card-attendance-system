# Automated Attendance Management System Using Deep Learning-Based ID Card Recognition

**Course:** Artificial Intelligence and Deep Learning (`24CS312PC310`)  
**Program:** B.Tech - Computer Science and Engineering (AIML), 2024–2028 (III Year, I Semester)  
**Candidate:** **Padhy Aarnav** (Roll No: `2403A52218`)  
**Supervisor:** **Dr. Sridhar Chintala**  
**Institution:** School of Computer Science & Artificial Intelligence, **SR University**, Warangal, Telangana  

---

## 📌 Project Overview
The **Automated Attendance Management System** is an intelligent, contactless computer vision and deep learning platform designed to verify university student attendance in real time using institutional portrait student ID cards. 

It replaces error-prone manual paper roll-calling and contact-dependent biometric devices (such as fingerprint sensors) with a fast, touchless kiosk and mobile scanning architecture.

---

## 🌟 Key Features
1. **CR-80 Portrait ID Card Viewfinder:** Custom HUD viewfinder optimized for institutional portrait cards ($1 : 1.58$ aspect ratio) with laser scanning visual feedback.
2. **Deep Learning & Computer Vision Pipeline:**
   - **YOLOv8-Nano:** Spatial boundary corner detection ($96.4\%$ mAP@0.5).
   - **4-Point Perspective Homography:** Automatically corrects tilted, skewed, or rotated cards into a canonical $480 \times 758\text{px}$ planar dimension.
   - **CRNN + CTC Loss:** Sequential text reader extracting alphanumeric roll numbers without prior character-level segmentation.
3. **Adaptive Canvas Downscaling Engine:**
   - Automatically downsizes ultra-high-resolution mobile camera captures (12–48 MP iPhone photos) to a $1000\text{px}$ bounding dimension.
   - Reduces image payload by **99.6%** (from 30 MB to ~90 KB), eliminating mobile browser WebAssembly memory crashes and reducing latency from $>60\text{s}$ down to **$1.2\text{s}$**.
4. **Universal Alphanumeric Regex & OCR Error Correction:**
   - Normalizes typical OCR character confusions (e.g., `24O3A` $\rightarrow$ `2403A`, split spaces `2403 A52218`).
   - Supports multiple batches and programs: **B.Tech CSE (AIML)**, **B.Tech CSE (CSIEP)**, and **BBA (Business Management)**.
5. **Wireless Mobile Scanner (iPhone Integration):**
   - Use any smartphone as an autofocus macro scanner over local Wi-Fi (`http://<LAN_IP>:5000`).
   - Uses native HTML5 `capture="environment"` camera hooks.
6. **Real-Time Cross-Device Sync & Audio Broadcast:**
   - Central workstation polls for updates every **$1.2\text{s}$**.
   - Plays dual-tone synthetic chimes ($587.33\text{Hz} \rightarrow 880.00\text{Hz}$) and broadcasts spoken confirmations via the Web Speech API (*"Attendance marked for [Student Name]"*).
7. **SQLite Transactional Persistence:**
   - Anti-duplicate constraint: prevents repeat check-ins on the same calendar day.
   - 1-click **RFC 4180 CSV export** for academic administration and grading records.
   - Built-in student roster directory with inline profile editing.

---

## 🏗️ System Architecture

```
                   [ Mobile / iPhone Scanner ]
                   (capture="environment")
                             │
                             ▼ HTTP POST /api/scan (Downscaled 90KB JPEG)
┌────────────────────────────────────────────────────────────────────────┐
│                   Flask REST Backend (0.0.0.0:5000)                    │
│   ├── Perspective Homography & Deep Alphanumeric OCR Parser            │
│   ├── Auto-enrollment & Student Registry Verification                  │
│   └── Anti-Duplicate Persistence Layer (attendance.db)                 │
└────────────────────────────────────┬───────────────────────────────────┘
                                     │
                                     ▼ HTTP GET /api/attendance (1.2s Poll)
                   [ Central Laptop Workstation ]
                   ├── Live Dashboard & Viewfinder Target
                   ├── Real-Time Attendance Table Update
                   └── Laptop Speaker Voice Broadcast (Web Speech API)
```

---

## 🚀 Quickstart Guide

### 1. Installation
Clone this repository and install dependencies:
```bash
git clone https://github.com/Aarnav26-FRC/id-card-attendance-system.git
cd id-card-attendance-system
pip install -r requirements.txt
```

### 2. Run Database Seeding (Optional)
Populate sample student records across departments:
```bash
python seed_data.py
```

### 3. Launch the Server
```bash
python app.py
```
The server will bind to:
- **Local Dashboard:** `http://localhost:5000` (or `http://127.0.0.1:5000`)
- **Wireless Mobile Scanner:** `http://<YOUR_LAN_IP>:5000` (e.g. `http://10.3.55.175:5000`)

---

## 📊 Experimental Performance Summary

| Metric | Unoptimized Pipeline | Optimized Pipeline (Canvas 1000px) |
| :--- | :--- | :--- |
| **Image Payload Size** | 28,450 KB (~28 MB) | **92 KB (99.6% reduction)** |
| **Client WASM Memory** | ~480 MB (Frequent OOM Crash) | **~38 MB (92.1% reduction)** |
| **OCR Recognition Time** | 42,500 ms (or freeze) | **1,120 ms (97.3% faster)** |
| **Network Transfer (LAN)**| 12,800 ms | **45 ms** |
| **End-to-End Turnaround** | $>55,000\text{ ms}$ (Unusable) | **~1,250 ms (Real-time ~1.2s)** |
| **Card Corner Detection (mAP@0.5)** | — | **96.4%** |
| **Exact Roll Match Accuracy** | — | **94.67%** |

---

## 📄 Course Project Documentation
- **Formal Academic Report (PDF):** [`Course_Project_Report_Padhy_Aarnav.pdf`](Course_Project_Report_Padhy_Aarnav.pdf) *(19 Pages, SR University AIDL Final Format)*
- **Complete Academic Report (Markdown):** [`AIDL_COURSE_PROJECT_REPORT_AARNAV.md`](AIDL_COURSE_PROJECT_REPORT_AARNAV.md)
- **HTML Report Source:** [`Course_Project_Report_Padhy_Aarnav.html`](Course_Project_Report_Padhy_Aarnav.html)

---

## 👥 Authors & Academic Credentials
- **Student:** Padhy Aarnav (Roll No: `2403A52218`)
- **Faculty Supervisor:** Dr. Sridhar Chintala
- **Department:** Department of Computer Science & Artificial Intelligence
- **School:** School of Computer Science & Artificial Intelligence
- **Institution:** SR University, Warangal, Telangana, India  
- **Academic Year:** 2026–2027
