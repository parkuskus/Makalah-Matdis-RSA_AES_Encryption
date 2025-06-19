from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from app.dbtocsv import export_users_to_csv

def run_export_gui():
    window = QWidget()
    window.setWindowTitle("📤 Export Data")
    window.resize(400, 250)

    layout = QVBoxLayout()
    layout.setContentsMargins(40, 40, 40, 40)
    layout.setSpacing(20)

    label = QLabel("📤 Export User Data to CSV")
    label.setFont(QFont("Segoe UI", 18, QFont.Bold))
    label.setAlignment(Qt.AlignCenter)
    layout.addWidget(label)

    export_button = QPushButton("Export Now")
    export_button.setFont(QFont("Segoe UI", 12, QFont.Bold))
    export_button.setCursor(Qt.PointingHandCursor)
    export_button.setStyleSheet("""
        QPushButton {
            background-color: #4CAF50;
            color: white;
            padding: 12px;
            border: none;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #388E3C;
        }
    """)

    def export_and_notify():
        try:
            filename = export_users_to_csv()
            QMessageBox.information(window, "Success", f"Data exported to '{filename}'")
        except Exception as e:
            QMessageBox.critical(window, "Export Failed", str(e))

    export_button.clicked.connect(export_and_notify)
    layout.addStretch()
    layout.addWidget(export_button)

    window.setLayout(layout)
    window.show()
