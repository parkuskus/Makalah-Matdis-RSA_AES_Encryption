from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from app.encryption import aes_encrypt_only, aes_decrypt_only

def run_text_cipher_gui():
    global window
    window = QWidget()
    window.setWindowTitle("🔐 Text ⇄ AES Cipher")
    window.resize(700, 600)

    layout = QVBoxLayout()
    layout.setContentsMargins(60, 60, 60, 60)
    layout.setSpacing(20)

    title = QLabel("🔐 AES Encryption & Decryption")
    title.setFont(QFont("Segoe UI", 20, QFont.Bold))
    title.setAlignment(Qt.AlignCenter)

    # Encrypt Section
    label_input = QLabel("🔤 Enter Plain Text")
    label_input.setFont(QFont("Segoe UI", 12))
    input_field = QLineEdit()
    input_field.setPlaceholderText("Type your message here...")
    input_field.setFont(QFont("Segoe UI", 12))
    input_field.setStyleSheet("""
        padding: 10px;
        border-radius: 8px;
        font-size: 16px;
    """)

    encrypt_button = QPushButton("🔒 Encrypt")
    encrypt_button.setFont(QFont("Segoe UI", 12, QFont.Bold))
    encrypt_button.setCursor(Qt.PointingHandCursor)
    encrypt_button.setStyleSheet("""
        QPushButton {
            background-color: #4c8bf5;
            color: white;
            padding: 12px;
            border: none;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #3367d6;
        }
    """)

    label_output = QLabel("🧾 Encrypted Result (Base64)")
    label_output.setFont(QFont("Segoe UI", 12))
    output_area = QTextEdit()
    output_area.setFont(QFont("Consolas", 10))
    output_area.setReadOnly(True)
    output_area.setStyleSheet("""
        padding: 10px;
        border-radius: 8px;
        background-color: #1e1e1e;
        color: #dcdcdc;
    """)

    def encrypt_text():
        plaintext = input_field.text().strip()
        if not plaintext:
            output_area.setText("⚠️ Please enter some text.")
            return
        cipher_b64, key_b64 = aes_encrypt_only(plaintext)
        output_area.setText(
            f"🧾 Cipher Text:\n{cipher_b64}\n\n🔑 AES Key:\n{key_b64}"
        )

    encrypt_button.clicked.connect(encrypt_text)

    # Decrypt Section
    label_cipher = QLabel("🔐 Cipher Text (Base64)")
    label_cipher.setFont(QFont("Segoe UI", 12))
    input_cipher = QLineEdit()
    input_cipher.setFont(QFont("Segoe UI", 12))
    input_cipher.setPlaceholderText("Paste encrypted text here...")
    input_cipher.setStyleSheet("padding: 10px; border-radius: 8px; font-size: 16px;")

    label_key = QLabel("🗝️ AES Key (Base64)")
    label_key.setFont(QFont("Segoe UI", 12))
    input_key = QLineEdit()
    input_key.setFont(QFont("Segoe UI", 12))
    input_key.setPlaceholderText("Paste AES key here...")
    input_key.setStyleSheet("padding: 10px; border-radius: 8px; font-size: 16px;")

    result_label = QLabel("📤 Decrypted Result")
    result_label.setFont(QFont("Segoe UI", 12))
    decrypted_output = QTextEdit()
    decrypted_output.setFont(QFont("Consolas", 10))
    decrypted_output.setReadOnly(True)
    decrypted_output.setStyleSheet("""
        padding: 10px;
        border-radius: 8px;
        background-color: #1e1e1e;
        color: #dcdcdc;
    """)

    decrypt_button = QPushButton("🔓 Decrypt")
    decrypt_button.setFont(QFont("Segoe UI", 12, QFont.Bold))
    decrypt_button.setCursor(Qt.PointingHandCursor)
    decrypt_button.setStyleSheet("""
        QPushButton {
            background-color: #4c8bf5;
            color: white;
            padding: 12px;
            border: none;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #3367d6;
        }
    """)

    def decrypt_text():
        try:
            plaintext = aes_decrypt_only(input_cipher.text().strip(), input_key.text().strip())
            decrypted_output.setText(f"✅ Plaintext:\n{plaintext}")
        except Exception as e:
            decrypted_output.setText(f"❌ Error: {str(e)}")

    decrypt_button.clicked.connect(decrypt_text)

    layout.addWidget(title)

    layout.addWidget(label_input)
    layout.addWidget(input_field)
    layout.addWidget(encrypt_button)
    layout.addWidget(label_output)
    layout.addWidget(output_area)

    layout.addWidget(label_cipher)
    layout.addWidget(input_cipher)
    layout.addWidget(label_key)
    layout.addWidget(input_key)
    layout.addWidget(decrypt_button)
    layout.addWidget(result_label)
    layout.addWidget(decrypted_output)

    window.setLayout(layout)
    window.show()
