import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play(user_choice):
    computer_choice = random.choice(choices)
    
    # Determine the result
    result = determine_winner(user_choice, computer_choice)

    user_choice_label.config(text=f"Your Choice: {user_choice.capitalize()}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice.capitalize()}")
    result_label.config(text=result)
    
    # Update the scores
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    
    # Display updated scores
    score_label.config(text=f"Score -> You: {user_score}, Computer: {computer_score}")

# Initialize the window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Choices
choices = ["rock", "paper", "scissors"]

# Initialize scores
user_score = 0
computer_score = 0

# Widgets for user and computer choices
user_choice_label = tk.Label(root, text="Your Choice: None", font=('Helvetica', 14))
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(root, text="Computer's Choice: None", font=('Helvetica', 14))
computer_choice_label.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=('Helvetica', 16, 'bold'))
result_label.pack(pady=20)

# Score label
score_label = tk.Label(root, text=f"Score -> You: {user_score}, Computer: {computer_score}", font=('Helvetica', 14))
score_label.pack(pady=10)

# Button Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Buttons for Rock, Paper, Scissors
rock_button = tk.Button(button_frame, text="Rock", font=('Helvetica', 12), command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=20)

paper_button = tk.Button(button_frame, text="Paper", font=('Helvetica', 12), command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=20)

scissors_button = tk.Button(button_frame, text="Scissors", font=('Helvetica', 12), command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=20)

# Start the GUI main loop
root.mainloop()