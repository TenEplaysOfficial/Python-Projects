import tkinter as tk
import random


def roll_dice():
    try:
        sides = int(sides_entry.get())  # Get the number of sides
        rolls = int(rolls_entry.get())  # Get the number of rolls
        
        if sides < 1 or rolls < 1:
            result_label.config(text="Please enter positive numbers for sides and rolls.")
            return
        
        results = [random.randint(1, sides) for _ in range(rolls)]  # Simulate dice rolls
        
        # Display the results
        result_label.config(text=f"Results: {', '.join(map(str, results))}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numeric values.")

# Main window
root = tk.Tk()
root.title("Dice Rolling Simulator")

# Instruction label
instruction_label = tk.Label(root, text="Enter the number of sides and rolls:", font=('Helvetica', 14))
instruction_label.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

sides_label = tk.Label(input_frame, text="Number of sides:", font=('Helvetica', 12))
sides_label.grid(row=0, column=0, padx=10)
sides_entry = tk.Entry(input_frame, font=('Helvetica', 12), width=5)
sides_entry.grid(row=0, column=1, padx=10)

rolls_label = tk.Label(input_frame, text="Number of rolls:", font=('Helvetica', 12))
rolls_label.grid(row=1, column=0, padx=10)
rolls_entry = tk.Entry(input_frame, font=('Helvetica', 12), width=5)
rolls_entry.grid(row=1, column=1, padx=10)

roll_button = tk.Button(root, text="Roll Dice", font=('Helvetica', 14), command=roll_dice)
roll_button.pack(pady=20)

result_label = tk.Label(root, text="", font=('Helvetica', 14))
result_label.pack(pady=20)

root.mainloop()