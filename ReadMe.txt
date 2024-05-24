EnigmaEase Password Management System
Developer: SK Hamim Ishthiaque Pranto
Email: hamimistiak22@gmail.com

Overview
EnigmaEase is a secure, efficient, and user-friendly password management system designed to help users generate, store, and retrieve passwords safely. The system utilizes Fernet symmetric encryption to ensure that all stored data is encrypted and protected from unauthorized access.
Features
* Password Generation: Generate strong, random passwords with customizable lengths.
* Password Storage: Securely store passwords, usernames, and website URLs in an encrypted JSON file.
* Password Retrieval: Easily search for and retrieve stored passwords.
* User-Friendly GUI: Intuitive graphical user interface built with Tkinter.
* Clipboard Integration: Copy generated and retrieved passwords directly to the clipboard.
Technical Details
Language
* Python 3.6 or above
Required Libraries
* tkinter for GUI
* cryptography for encryption (Fernet)
* json for data storage
* pyperclip for clipboard integration
* random for password generation
Environment Setup
1. Install Python:
* Ensure Python 3.6 or above is installed on your system. You can download it from python.org.
2. Install Required Libraries:
* Open your terminal or command prompt and run the following command:
bash
Copy code
pip install cryptography pyperclip 
Setup Instructions
1. Download or Clone the Project:
* Download the project files or clone the repository to your desired directory:
git clone EnigmaEase-Password_Management_System/main.py at master   Sk-Hamim-Ishthiaque-Pranto/EnigmaEase-Password_Management_System (github.com)
2. Run the Application:
* Navigate to the project directory and run the script:
cd EnigmaEase python your_script_name.py 
How to Use
Generating a Password
1. Open EnigmaEase.
2. Set the desired password length using the "Password Size" scale.
3. Click the "Generate Password" button.
4. The generated password will appear in the password field and be copied to the clipboard.
Saving a Password
1. Enter the website title in the "Website" field.
2. Enter the URL in the "Website URL" field.
3. Enter the username/email in the "Email/Username" field.
4. Enter the password in the "Password" field.
5. Click the "Add" button to save the entry. The data will be encrypted and stored securely.
Retrieving a Password
1. Enter the website title in the "Website" field.
2. Click the "Search" button.
3. If the website title exists, the username, URL, and password will be displayed in a message box and the password will be copied to the clipboard.
Future Enhancements
* Cloud Synchronization: Sync passwords across multiple devices.
* Multi-User Support: Allow multiple users to have their own password entries.
* Two-Factor Authentication (2FA): Add an additional layer of security.
* Password Strength Analysis: Provide feedback on the strength of generated and stored passwords.
Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

