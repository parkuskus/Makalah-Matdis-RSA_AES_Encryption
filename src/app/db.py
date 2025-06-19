import sqlite3
import os

def connect_db():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect("data/users.db")

def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            place_of_birth TEXT,
            date_of_birth TEXT,
            gpa REAL,
            username TEXT UNIQUE,
            encrypted_password BLOB,
            encrypted_key BLOB
        )
    ''')
    conn.commit()
    conn.close()

def insert_user(data):
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute('''
            INSERT INTO users 
            (name, place_of_birth, date_of_birth, username, gpa, encrypted_password, encrypted_key)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', data)
        conn.commit()
    except sqlite3.IntegrityError as e:
        raise ValueError("Username already exists.")
    finally:
        conn.close()

def get_user_by_username(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, place_of_birth, date_of_birth, gpa, username,
               encrypted_password, encrypted_key
        FROM users WHERE username = ?
    """, (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_all_users_sorted(by="name", order="asc"):
    conn = connect_db()
    cursor = conn.cursor()

    # Validasi kolom & urutan
    if by not in ["name", "gpa"]:
        by = "name"
    if order not in ["asc", "desc"]:
        order = "asc"

    cursor.execute(f"""
        SELECT name, place_of_birth, date_of_birth, username, gpa
        FROM users
        ORDER BY {by} {order.upper()}
    """)
    results = cursor.fetchall()
    conn.close()
    return results
