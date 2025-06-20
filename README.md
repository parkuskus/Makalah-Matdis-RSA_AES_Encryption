# 🔐 Enhancing Protection for Database Management System via Encryption using Rivest-Shamir-Adleman (RSA) and Advanced Encryption Standard (AES) Algorithm
This project is a GUI-based database management system (DBMS) application built with Python. In this application, administrator can register accounts, log in, and have their data stored securely using RSA and AES encryption. Admins can also export user data to CSV files for auditing or documentation.

## ✨ Features
This application includes several essential features similar to what you'd expect in real-world secure login systems:
1. User Registration & Login : users can register and log in using an intuitive and user-friendly interface.
2. Password Strength Evaluation: the system evaluates the strength of user passwords during registration.
3. Secure Data Encryption: passwords are encrypted using a hybrid AES + RSA approach before being stored.
4. Admin Dashboard: admins have a dedicated interface to view and manage users.
5. Export to CSV: user data can be exported to a CSV file (exported_users.csv) via the admin panel.

## 🛠️ Installation
### Prerequisites
Make sure you have Python 3.12+ installed along with the following packages:
```bash
pip install pyqt5 pycryptodome
```

### How to Run
1. Clone this repository
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name/src
   ```
2. Run the application:
   ```bash
   python main.py
   ```
3. Done! The login window will appear, and you can start using the system.

## 📁 Directory Structure
```
src/
├── app/
│   ├── db.py                  # Database initialization and operations
│   ├── encryption.py          # AES + RSA encryption logic
│   ├── password_strength.py   # Password strength scoring
│   └── dbtocsv.py             # Export users to CSV
├── gui/
│   ├── login_gui.py           # Login screen
│   ├── register_gui.py        # Registration screen
│   ├── main_menu_gui.py       # Main menu
│   ├── admin_profile_gui.py   # Admin panel
│   └── export_gui.py          # Export interface
├── data/
│   ├── users.db               # SQLite user database
│   ├── public.pem             # RSA public key
│   └── private.pem            # RSA private key
├── exported_users.csv         # Exported user data
├── itb_logo.png               # Logo for UI
└── main.py                    # Application entry point
```

## 🤝 How to Contribute
1. Fork this repository
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "This is my feature"
   ```
4. Push the changes to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a new pull request. If the feature meet the criteria, your feature will be considered to be included in the project!

## License
This project is licensed under the <u><a href="https://github.com/parkuskus/Makalah-Matdis-RSA_AES_Encryption/blob/main/LICENSE">MIT</a></u> License.
