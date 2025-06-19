from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

user_profile_window = None

def show_user_profile(user_data):
    name, pob, dob, username = user_data
    global user_profile_window
    user_profile_window = QWidget()
    user_profile_window.setWindowTitle("👤 User Profile")
    user_profile_window.resize(400, 300)

    layout = QVBoxLayout()
    layout.setContentsMargins(30, 30, 30, 30)
    layout.setSpacing(15)

    title = QLabel("👤 Logged In User Information")
    title.setFont(QFont("Segoe UI", 16, QFont.Bold))
    title.setAlignment(Qt.AlignCenter)
    layout.addWidget(title)

    fields = ["Name", "Place of Birth", "Date of Birth", "Username"]
    for label_text, value in zip(fields, user_data):
        label = QLabel(f"{label_text}: {value}")
        label.setFont(QFont("Segoe UI", 12))
        layout.addWidget(label)

    user_profile_window.setLayout(layout)
    user_profile_window.show()
