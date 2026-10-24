import tkinter as tk
from datetime import datetime


# ==========================================
# KEYLOGGER FUNCTIONS
# ==========================================

log_file = "keylog.txt"


def log_key(event):
    """Record a key pressed inside this application."""

    key = event.keysym

    # Convert special keys into readable text
    if key == "space":
        key_text = "[SPACE]"
    elif key == "Return":
        key_text = "[ENTER]"
    elif key == "BackSpace":
        key_text = "[BACKSPACE]"
    elif key == "Tab":
        key_text = "[TAB]"
    elif key == "Shift_L" or key == "Shift_R":
        key_text = "[SHIFT]"
    elif key == "Control_L" or key == "Control_R":
        key_text = "[CTRL]"
    elif key == "Alt_L" or key == "Alt_R":
        key_text = "[ALT]"
    elif len(key) == 1:
        key_text = key
    else:
        key_text = f"[{key.upper()}]"

    # Display the key on screen
    display.insert(tk.END, key_text)
    display.see(tk.END)

    # Save key to file
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(key_text)


# ==========================================
# START LOGGING SESSION
# ==========================================

def start_logging():

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(log_file, "a", encoding="utf-8") as file:
        file.write(
            f"\n\n--- Logging Session: {timestamp} ---\n"
        )

    status.config(text="Logging: ACTIVE")

    text_area.focus_set()


# ==========================================
# STOP LOGGING
# ==========================================

def stop_logging():

    status.config(text="Logging: STOPPED")

    with open(log_file, "a", encoding="utf-8") as file:
        file.write("\n--- Logging stopped ---\n")


# ==========================================
# MAIN WINDOW
# ==========================================

window = tk.Tk()

window.title("Educational Keylogger")
window.geometry("650x450")

title = tk.Label(
    window,
    text="Educational Keylogger",
    font=("Arial", 20, "bold")
)

title.pack(pady=15)


description = tk.Label(
    window,
    text="This program records keys typed inside this window only.",
    font=("Arial", 11)
)

description.pack(pady=5)


status = tk.Label(
    window,
    text="Logging: STOPPED",
    font=("Arial", 12)
)

status.pack(pady=10)


# ==========================================
# TEXT AREA
# ==========================================

text_area = tk.Text(
    window,
    height=8,
    width=60,
    font=("Arial", 12)
)

text_area.pack(pady=10)


# ==========================================
# LOG DISPLAY
# ==========================================

display = tk.Text(
    window,
    height=6,
    width=60,
    font=("Courier", 10)
)

display.pack(pady=10)


# ==========================================
# BUTTONS
# ==========================================

start_button = tk.Button(
    window,
    text="Start Logging",
    command=start_logging
)

start_button.pack(side=tk.LEFT, padx=150, pady=10)


stop_button = tk.Button(
    window,
    text="Stop Logging",
    command=stop_logging
)

stop_button.pack(side=tk.RIGHT, padx=150, pady=10)


# ==========================================
# KEY EVENT
# ==========================================

text_area.bind("<KeyPress>", log_key)


# ==========================================
# START APPLICATION
# ==========================================

window.mainloop()