import pickle
import os
from deepface import DeepFace
from src.database.db_manager import DatabaseManager

def generate():
    db = DatabaseManager()
    db.cursor.execute("SELECT student_id, image_path FROM students WHERE embedding_vector IS NULL")
    rows = db.cursor.fetchall()
    for s_id, path in rows:
        try:
            objs = DeepFace.represent(img_path=os.path.abspath(path), model_name='Facenet', enforce_detection=False, detector_backend='skip')
            embedding_blob = pickle.dumps(objs[0]['embedding'])
            db.cursor.execute("UPDATE students SET embedding_vector = ? WHERE student_id = ?", (embedding_blob, s_id))
            db.conn.commit()
            print(f"✅ Embedding Done for {s_id}")
        except Exception as e: print(f"❌ Error: {e}")

if __name__ == "__main__": generate()
