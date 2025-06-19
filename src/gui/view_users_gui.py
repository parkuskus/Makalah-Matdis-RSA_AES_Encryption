from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from app.db import get_all_users_sorted

def run_view_users_gui():
    global window
    window = QWidget()
    window.setWindowTitle("👥 View Users")
    window.resize(800, 500)

    layout = QVBoxLayout()
    layout.setContentsMargins(40, 40, 40, 40)
    layout.setSpacing(20)

    title = QLabel("👥 User List (Sortable)")
    title.setFont(QFont("Segoe UI", 18, QFont.Bold))
    title.setAlignment(Qt.AlignCenter)

    layout.addWidget(title)

    # Dropdown filter
    sort_combo = QComboBox()
    sort_combo.setFont(QFont("Segoe UI", 12))
    sort_combo.addItems([
        "Name (A-Z)", "Name (Z-A)", "GPA (Lowest First)", "GPA (Highest First)"
    ])
    layout.addWidget(sort_combo)

    # Tabel
    table = QTableWidget()
    table.setColumnCount(5)
    table.setHorizontalHeaderLabels(["Name", "Place of Birth", "Date of Birth", "Username", "GPA"])
    table.setStyleSheet("font-size: 12px;")
    layout.addWidget(table)

    def update_table():
        selected = sort_combo.currentText()
        if selected == "Name (A-Z)":
            users = get_all_users_sorted(by="name", order="asc")
        elif selected == "Name (Z-A)":
            users = get_all_users_sorted(by="name", order="desc")
        elif selected == "GPA (Lowest First)":
            users = get_all_users_sorted(by="gpa", order="asc")
        else:
            users = get_all_users_sorted(by="gpa", order="desc")

        table.setRowCount(len(users))
        for row_idx, user in enumerate(users):
            for col_idx, val in enumerate(user):
                table.setItem(row_idx, col_idx, QTableWidgetItem(str(val)))

    sort_combo.currentIndexChanged.connect(update_table)
    update_table()  # Load awal

    window.setLayout(layout)
    window.show()
