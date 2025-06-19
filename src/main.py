from app.db import init_db
from gui.login_gui import launch_login
from scripts.dummy_data import insert_dummy_data, insert_admin_user  # ← import dummy_data.py

if __name__ == "__main__":
    init_db()
    insert_admin_user()
    insert_dummy_data(n=10)  # ← tambahkan dummy data
    launch_login()