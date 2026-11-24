import sqlite3

def setup_database():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll_number TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            year TEXT NOT NULL,
            section TEXT NOT NULL
        )
    """)

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

    students = [
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
        ("2403A54055", "Eshwar Varma", "BTech - CSE - AIML", "2024-2028", "Section B"),
        ("2403A54060", "Farhan Ali", "BTech - CSE - AIML", "2024-2028", "Section B")
    ]

    cursor.executemany("""
        INSERT OR REPLACE INTO students (roll_number, name, department, year, section)
        VALUES (?, ?, ?, ?, ?)
    """, students)

    conn.commit()
    conn.close()
    print("[SUCCESS] Database 'attendance.db' initialized with sample student registry.")

if __name__ == "__main__":
    setup_database()
