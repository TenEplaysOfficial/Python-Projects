import tkinter as tk
import random

# Word list for Hangman
word_list = ["python", "hangman", "programming", "developer", "interface", "computer", "random", "graphics"]

# Function to select a random word
def choose_word():
    return random.choice(word_list).lower()

# Game state
def initialize_game():
    global selected_word, guessed_word, attempts, guessed_letters
    
    selected_word = choose_word()  # Random word
    guessed_word = ["_" for _ in selected_word]  # Empty underscores for unguessed letters
    attempts = 6  # Number of wrong guesses allowed
    guessed_letters = []  # List to store guessed letters
    
    update_display()
    hangman_label.config(text="Hangman: You have 6 attempts!")
    word_label.config(text=" ".join(guessed_word))
    letters_label.config(text="Guessed Letters: ")

#Update the hangman figure and game state
def update_display():
    hangman_figures = [
        "6 attempts left",
        "5 attempts left",
        "4 attempts left",
        "3 attempts left",
        "2 attempts left",
        "1 attempt left",
        "No attempts left - Game Over!"    
        ]
    hangman_label.config(text=hangman_figures[6 - attempts])

# Handle letter guesses
def guess_letter():
    global attempts
    
    letter = entry.get().lower()  # Get the letter from the input
    entry.delete(0, tk.END)  # Clear the input field
    
    if letter in guessed_letters or len(letter) != 1 or not letter.isalpha():
        feedback_label.config(text="Invalid guess or already guessed. Try again!")
        return
    
    guessed_letters.append(letter)
    letters_label.config(text="Guessed Letters: " + ", ".join(guessed_letters))
    
    if letter in selected_word:
        # Update guessed word
        for i, char in enumerate(selected_word):
            if char == letter:
                guessed_word[i] = letter
        word_label.config(text=" ".join(guessed_word))
        feedback_label.config(text="Good guess!")
        
        if "_" not in guessed_word:
            feedback_label.config(text="Congratulations! You've won!")
            play_again_prompt()
    else:
        attempts -= 1
        update_display()
        feedback_label.config(text="Incorrect guess!")
        
        if attempts == 0:
            feedback_label.config(text=f"Game over! The word was '{selected_word}'.")
            play_again_prompt()

# Play again
def play_again_prompt():
    play_again_button.config(state=tk.NORMAL)

# Reset the game when the user chooses to play again
def play_again():
    play_again_button.config(state=tk.DISABLED)
    initialize_game()

# Main window
root = tk.Tk()
root.title("Hangman Game")

# Labels to display the hangman status and word state
hangman_label = tk.Label(root, text="", font=('Helvetica', 14))
hangman_label.pack(pady=10)

word_label = tk.Label(root, text="", font=('Helvetica', 20, 'bold'))
word_label.pack(pady=10)

letters_label = tk.Label(root, text="Guessed Letters: ", font=('Helvetica', 14))
letters_label.pack(pady=10)

feedback_label = tk.Label(root, text="", font=('Helvetica', 14), fg="red")
feedback_label.pack(pady=10)

entry = tk.Entry(root, font=('Helvetica', 14), width=3)
entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", font=('Helvetica', 14), command=guess_letter)
guess_button.pack(pady=10)

play_again_button = tk.Button(root, text="Play Again", font=('Helvetica', 14), command=play_again)
play_again_button.pack(pady=10)
play_again_button.config(state=tk.DISABLED)

initialize_game()

root.mainloop()