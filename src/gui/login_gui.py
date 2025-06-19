from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox, QFrame
)
import sys
from app.encryption import decrypt_sensitive_fields
from app.db import get_user_by_username
from gui.main_menu_gui import show_main_menu

def login(entry_username, entry_password, window):
    username = entry_username.text()
    password_input = entry_password.text()

    result = get_user_by_username(username)
    if result:
        id, name, pob, dob, gpa, username, encrypted_password, encrypted_key = result
        try:
            password, *_ = decrypt_sensitive_fields(encrypted_password, encrypted_key)
            if password == password_input:
                QMessageBox.information(window, "Login", "Login successful!")
                window.close()

                # Kirim data pengguna ke main menu
                from gui.main_menu_gui import show_main_menu
                show_main_menu((name, pob, dob, username))
            else:
                QMessageBox.critical(window, "Login", "Incorrect password")
        except:
            QMessageBox.critical(window, "Login", "Decryption error")
    else:
        QMessageBox.critical(window, "Login", "User not found")

def launch_login():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    dark_palette = QtGui.QPalette()
    dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(45, 45, 45))
    dark_palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(30, 30, 30))
    dark_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(45, 45, 45))
    dark_palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    dark_palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    dark_palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(45, 45, 45))
    dark_palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    dark_palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    dark_palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
    dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
    dark_palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(dark_palette)

    window = QWidget()
    window.setWindowTitle("🔐 Secure Login")
    window.resize(600, 500)
    window.setWindowIcon(QtGui.QIcon("lock_icon.png"))

    layout = QVBoxLayout()
    layout.setContentsMargins(60, 60, 60, 60)
    layout.setSpacing(30)

    logo = QLabel()
    pixmap = QtGui.QPixmap("itb_logo.png")
    pixmap = pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
    logo.setPixmap(pixmap)
    logo.setAlignment(QtCore.Qt.AlignCenter)

    title = QLabel("🔐 Secure Database Management System")
    title.setFont(QtGui.QFont("Segoe UI", 20, QtGui.QFont.Bold))
    title.setAlignment(QtCore.Qt.AlignCenter)

    label_username = QLabel("Username")
    label_username.setFont(QtGui.QFont("Segoe UI", 12))
    entry_username = QLineEdit()
    entry_username.setPlaceholderText("Enter your username")
    entry_username.setStyleSheet("padding: 10px; border-radius: 8px; font-size: 16px")

    label_password = QLabel("Password")
    label_password.setFont(QtGui.QFont("Segoe UI", 12))
    entry_password = QLineEdit()
    entry_password.setEchoMode(QLineEdit.Password)
    entry_password.setPlaceholderText("Enter your password")
    entry_password.setStyleSheet("padding: 10px; border-radius: 8px; font-size: 16px")

    login_button = QPushButton("Login")
    login_button.setFont(QtGui.QFont("Segoe UI", 12, QtGui.QFont.Bold))
    login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    login_button.setStyleSheet(
        "QPushButton { background-color: #2e86de; color: white; padding: 12px; border: none; border-radius: 8px; }"
        "QPushButton:hover { background-color: #1b4f72; }"
    )
    login_button.clicked.connect(lambda: login(entry_username, entry_password, window))

    layout.addWidget(logo)
    layout.addWidget(title)
    layout.addWidget(label_username)
    layout.addWidget(entry_username)
    layout.addWidget(label_password)
    layout.addWidget(entry_password)
    layout.addStretch()
    layout.addWidget(login_button)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())
