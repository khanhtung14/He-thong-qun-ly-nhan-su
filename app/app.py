import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "postgres"),
        database=os.getenv("DB_NAME", "hrm_db"),
        user=os.getenv("DB_USER", "hrm_user"),
        password=os.getenv("DB_PASSWORD", "SuperSecurePassword123!")
    )

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "service": "Human Resource Management System (HRM)",
        "modules": ["Quan ly Nhan vien", "Quan ly Phong ban", "Cham cong"]
    })

@app.route('/health')
def health():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()[0]
        cur.close()
        conn.close()
        return jsonify({
            "status": "UP",
            "database_connection": "Successful",
            "postgres_version": db_version
        }), 200
    except Exception as e:
        return jsonify({
            "status": "DOWN",
            "database_connection": "Failed",
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
