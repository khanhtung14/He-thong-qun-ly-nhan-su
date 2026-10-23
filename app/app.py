import os
import psycopg2
from flask import Flask, jsonify, render_template

app = Flask(__name__)

DB_HOST = os.environ.get('DB_HOST', 'postgres')
DB_NAME = os.environ.get('DB_NAME', 'hrm_db')
DB_USER = os.environ.get('DB_USER', 'hrm_user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'StrongPasswordForHRM2026!')

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route('/')
def home():
    # Render giao diện HTML Bootstrap
    return render_template('index.html')

@app.route('/health')
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({
            "status": "healthy",
            "database_connection": "Successful",
            "application": "HRM System (De 10)",
            "proxy_protocol": "HTTPS"
        }), 200
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "database_connection": "Failed",
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
