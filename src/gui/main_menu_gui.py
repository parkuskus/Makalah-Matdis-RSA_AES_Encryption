from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from gui import register_gui
from gui import admin_profile_gui
from gui import text_to_cipher_gui
from gui import export_gui
from gui import view_users_gui

# Add a global variable to keep the window from disappearing immediately
main_menu_window = None

def show_main_menu(user_data):
    global main_menu_window  # important: save to global variable

    main_menu_window = QWidget()
    main_menu_window.setWindowTitle("Dashboard")
    main_menu_window.resize(500, 400)

    layout = QVBoxLayout()
    layout.setSpacing(20)
    layout.setContentsMargins(40, 40, 40, 40)

    label = QLabel("🎛️ Main Menu")
    label.setFont(QFont("Segoe UI", 18, QFont.Bold))
    label.setAlignment(Qt.AlignCenter)
    layout.addWidget(label)

    btn_register = QPushButton("📝 Register New User")
    btn_register.clicked.connect(lambda: register_gui.run_register_gui())
    layout.addWidget(btn_register)

    btn_about = QPushButton("ℹ️ About")
    btn_about.clicked.connect(lambda: admin_profile_gui.show_user_profile(user_data))
    layout.addWidget(btn_about)
    
    btn_textTocipher = QPushButton("🛡️ Text to Cipher")
    btn_textTocipher.clicked.connect(lambda: text_to_cipher_gui.run_text_cipher_gui())
    layout.addWidget(btn_textTocipher)
    
    btn_export = QPushButton("📤 Export Users to CSV")
    btn_export.clicked.connect(lambda: export_gui.run_export_gui())
    layout.addWidget(btn_export)

    btn_view_users = QPushButton("👥 View All Users")
    btn_view_users.clicked.connect(lambda: view_users_gui.run_view_users_gui())
    layout.addWidget(btn_view_users)

    btn_logout = QPushButton("🚪 Logout")
    btn_logout.clicked.connect(main_menu_window.close)
    layout.addWidget(btn_logout)


    for btn in [btn_register, btn_about, btn_logout, btn_textTocipher, btn_export, btn_view_users]:
        btn.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                padding: 12px;
                border-radius: 8px;
                background-color: #4c8bf5;
                color: white;
            }
            QPushButton:hover {
                background-color: #3367d6;
            }
        """)

    main_menu_window.setLayout(layout)
    main_menu_window.show()
