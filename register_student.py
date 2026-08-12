import cv2
import os
from src.database.db_manager import DatabaseManager

def register():
    db = DatabaseManager()
    s_id = input("ID: "); s_name = input("Name: "); dept = input("Dept: ")
    os.makedirs(f"dataset/{s_id}", exist_ok=True)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        ret, frame = cap.read()
        cv2.imshow("Press 's' to Save", frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            path = f"dataset/{s_id}/{s_id}.jpg"
            cv2.imwrite(path, frame)
            db.cursor.execute("INSERT INTO students (student_id, student_name, department, image_path) VALUES (?,?,?,?)", (s_id, s_name, dept, path))
            db.conn.commit()
            print("✅ Registered"); break
    cap.release(); cv2.destroyAllWindows()

if __name__ == "__main__": register()
