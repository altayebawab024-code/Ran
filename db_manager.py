import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path="database/attendance_system.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS students (student_id TEXT PRIMARY KEY, student_name TEXT, department TEXT, image_path TEXT, embedding_vector BLOB)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS attendance (attendance_id INTEGER PRIMARY KEY AUTOINCREMENT, student_id TEXT, course_id TEXT, date TEXT, time TEXT, status TEXT, confidence_score REAL, UNIQUE(student_id, date))')
        self.conn.commit()

if __name__ == "__main__":
    db = DatabaseManager()
    print("✅ DB Ready")
