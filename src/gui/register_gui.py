from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox
)
import sys
import re
from app.encryption import encrypt_sensitive_fields
from app.db import insert_user
from app.password_strength import evaluate_password_strength


def register(entry_name, entry_pob, entry_dob, entry_username, entry_gpa, entry_password, window):
    name = entry_name.text()
    pob = entry_pob.text()
    dob = entry_dob.text()
    gpa = entry_gpa.text()
    username = entry_username.text()
    password = entry_password.text()

    if not all([name, pob, dob, username, gpa, password]):
        QMessageBox.critical(window, "Register", "All fields must be filled")
        return

    try:
        encrypted_data, encrypted_key = encrypt_sensitive_fields(password)
        insert_user((name, pob, dob, gpa, username, encrypted_data, encrypted_key))
        QMessageBox.information(window, "Register", "Registration successful!")
        window.close()
    except Exception as e:
        QMessageBox.critical(window, "Register", f"Registration failed: {e}")

def run_register_gui():
    window = QWidget()
    window.setWindowTitle("Register")
    window.resize(600, 700)

    layout = QVBoxLayout()
    layout.setContentsMargins(60, 60, 60, 60)
    layout.setSpacing(20)

    title = QLabel("📝 Register User")
    title.setFont(QtGui.QFont("Segoe UI", 20, QtGui.QFont.Bold))
    title.setAlignment(QtCore.Qt.AlignCenter)

    def create_input(label_text):
        label = QLabel(label_text)
        label.setFont(QtGui.QFont("Segoe UI", 12))
        entry = QLineEdit()
        entry.setStyleSheet("""
            padding: 10px;
            border-radius: 8px;
            font-size: 16px;
        """)
        layout.addWidget(label)
        layout.addWidget(entry)
        return entry

    entry_name = create_input("Name")
    entry_pob = create_input("Place of Birth")
    entry_dob = create_input("Date of Birth (YYYY-MM-DD)")
    entry_username = create_input("Username")
    entry_gpa = create_input("GPA")

    label_password = QLabel("Password")
    label_password.setFont(QtGui.QFont("Segoe UI", 12))
    entry_password = QLineEdit()

    entry_password.setEchoMode(QLineEdit.Password)
    entry_password.setStyleSheet("""
    padding: 10px;
    border-radius: 8px;
    font-size: 16px;
    """)

    layout.addWidget(label_password)
    layout.addWidget(entry_password)

    password_strength_label = QLabel("Strength: ")
    password_strength_label.setFont(QtGui.QFont("Segoe UI", 10))
    layout.addWidget(password_strength_label)
    

    register_button = QPushButton("Register")
    register_button.setFont(QtGui.QFont("Segoe UI", 12, QtGui.QFont.Bold))
    def on_password_change():
        password = entry_password.text()
        strength, color = evaluate_password_strength(password)
        password_strength_label.setText(f"Strength: {strength}")
        password_strength_label.setStyleSheet(f"color: {color}; font-weight: bold;")
    # Connect it to text change
    entry_password.textChanged.connect(on_password_change)
    register_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    register_button.setStyleSheet(
        "QPushButton { background-color: #28a745; color: white; padding: 12px; border: none; border-radius: 8px; }"
        "QPushButton:hover { background-color: #218838; }"
    )
    register_button.clicked.connect(lambda: register(
        entry_name, entry_pob, entry_dob, entry_gpa,
        entry_username, entry_password, window
    ))

    layout.addStretch()
    layout.addWidget(register_button)

    window.setLayout(layout)
    window.show()

