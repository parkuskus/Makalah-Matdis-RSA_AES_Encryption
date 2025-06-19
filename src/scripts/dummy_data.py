from faker import Faker
from app.encryption import encrypt_sensitive_fields
from app.db import insert_user, get_user_by_username
import random

fake = Faker()

def insert_dummy_data(n=10):
    for _ in range(n):
        name = fake.name()
        pob = fake.city()
        dob = str(fake.date_of_birth(minimum_age=18, maximum_age=60))
        username = fake.user_name() + str(random.randint(100, 999))
        gpa = round(random.uniform(0.0, 4.0), 2)  # Generate GPA (0.00 to 4.00)
        password = fake.password()

        encrypted_data, encrypted_key = encrypt_sensitive_fields(password)
        try:
            insert_user((name, pob, dob, username, gpa, encrypted_data, encrypted_key))
        except ValueError:
            continue  # skip if username already exists

    print("Dummy users added.")

def insert_admin_user():
    if get_user_by_username("aufarksma") is None:
        name = "Muhammad Aufar Rizqi Kusuma"
        pob = "Bekasi"
        dob = "2006-07-02"
        username = "aufarksma"
        password = "aufar12345"
        gpa = 4.0  # Admin GPA

        encrypted_password, encrypted_key = encrypt_sensitive_fields(password)
        insert_user((name, pob, dob, username, gpa, encrypted_password, encrypted_key))
        print("[+] Admin user 'aufarksma' added.")
    else:
        print("[i] Admin user 'aufarksma' already exists.")
