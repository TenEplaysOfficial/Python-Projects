import tkinter as tk
from tkinter import messagebox
import time

def start_timer():
    try:
        total_seconds = int(entry.get())
        if total_seconds < 0:
            raise ValueError("Invalid time")

        start_button.config(state=tk.DISABLED)
        
        # Countdown loop
        while total_seconds > 0:
            minutes, seconds = divmod(total_seconds, 60)
            time_display = f"{minutes:02}:{seconds:02}"
            time_label.config(text=time_display)
            root.update()
            time.sleep(1)
            total_seconds -= 1

        time_label.config(text="00:00")
        messagebox.showinfo("Time's up!", "The countdown has ended!")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive number.")
    finally:
        start_button.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Countdown Timer")

instruction_label = tk.Label(root, text="Enter time in seconds:", font=('Helvetica', 14))
instruction_label.pack(pady=10)

entry = tk.Entry(root, font=('Helvetica', 14), width=10)
entry.pack(pady=10)

time_label = tk.Label(root, text="00:00", font=('Helvetica', 48), fg="red")
time_label.pack(pady=20)

start_button = tk.Button(root, text="Start Timer", font=('Helvetica', 14), command=start_timer)
start_button.pack(pady=20)

root.mainloop()