# consent_keycapture.py
# Use only on your own machine or with explicit consent of users.
# This app captures keystrokes only when the window is focused.

import tkinter as tk
from datetime import datetime

LOGFILE = "keycapture_consent.txt"

def on_key(event):
    # Record visible representation and timestamp
    key_repr = event.keysym  # e.g., 'a', 'Return', 'space'
    timestamp = datetime.utcnow().isoformat() + "Z"
    line = f"{timestamp}\t{key_repr}\n"
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(line)
    # show in UI for transparency
    txt.insert("end", f"{timestamp}  {key_repr}\n")
    txt.see("end")

root = tk.Tk()
root.title("Consented Key Capture — Only while focused")

lbl = tk.Label(root, text="This window captures keystrokes only while focused.\nPress keys to see them logged.")
lbl.pack(padx=10, pady=(10,0))

txt = tk.Text(root, height=15, width=60)
txt.pack(padx=10, pady=10)

info = tk.Label(root, text=f"Log file: {LOGFILE}")
info.pack(padx=10, pady=(0,10))

# Bind key events to the window (works only when this window is focused)
root.bind_all("<Key>", on_key)

root.mainloop()
