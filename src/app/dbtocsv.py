import csv
from app.db import connect_db

def export_users_to_csv(filename="exported_users.csv"):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, place_of_birth, date_of_birth, username, gpa
        FROM users
    """)
    users = cursor.fetchall()
    conn.close()

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Place of Birth", "Date of Birth", "Username", "GPA"])
        writer.writerows(users)

    return filename
