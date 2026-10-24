# PRODIGY_CS_04

# ⌨️ Simple Keylogger

## 📌 Project Overview
The Simple Keylogger is a Python-based educational application designed to demonstrate how keyboard input can be captured and recorded within an application.

For safety and privacy, this implementation records keystrokes only when the user types inside its own application window. It does not monitor other applications or capture system-wide keyboard activity.

## 🎯 Objectives
- Understand keyboard event handling in Python.
- Learn how applications process keyboard input.
- Practice event-driven programming.
- Understand the importance of privacy and responsible cybersecurity practices.

## ✨ Features
- **Keyboard Input Capture:** Captures key presses within its own application window.
- **Text Recording:** Records user input during the active session.
- **File Output:** Saves recorded input to `keylog.txt` (if enabled in the implementation).
- **Application-Only Monitoring:** Does not capture keystrokes from other applications.
- **User-Controlled Operation:** Runs as a visible application.

## 🛠️ Technologies Used
- Python 3
- Tkinter (GUI)
- Python Standard Library
  - `tkinter`
  - `datetime` (if used)

## 📁 Project Structure
```text
PRODIGY_CS_04/
│
├── keylogger.py
├── keylog.txt
├── README.md
└── LICENSE
```

*Note: `keylog.txt` is generated when the program runs, if file logging is enabled. It does not need to be included in the repository.*

## 🚀 Getting Started

### Prerequisites
- Python 3 installed on your system.
- Tkinter available in your Python installation.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/anonberry/PRODIGY_CS_04.git
   ```

2. Navigate into the project directory:
   ```bash
   cd PRODIGY_CS_04
   ```

3. Run the program:
   ```bash
   python keylogger.py
   ```

## 💻 Usage
1. Launch the application.
2. Click inside the application's input area.
3. Type a few test characters.
4. Observe how keyboard input is processed.
5. Check the generated output file, if file recording is enabled.

## ⚙️ How It Works
1. The application creates a visible GUI window.
2. The user types into the application's input area.
3. Keyboard events are handled by the application.
4. The program processes the captured input.
5. If configured, the input is written to a local text file.

## 🔒 Security & Ethical Considerations
- This project is intended strictly for educational purposes.
- Keystrokes are captured only within the application's own window.
- The program should not collect passwords, sensitive personal information, or confidential data.
- Users should be informed whenever input recording is enabled.
- Recorded data should be handled responsibly and deleted when no longer needed.
- System-wide keyboard monitoring, stealth operation, and unauthorized surveillance are outside the scope of this project.

## 📚 Learning Outcomes
- Understanding keyboard event handling.
- Introduction to GUI development using Tkinter.
- Practical experience with event-driven programming.
- Understanding privacy, consent, and ethical boundaries in cybersecurity.

## 👨‍💻 Author
**anonberry**

GitHub: [@anonberry](https://github.com/anonberry)

## 📄 License
This project is licensed under the MIT License.
