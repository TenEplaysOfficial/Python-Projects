import random
import string

def generate_password(length, complexity):

    if complexity == 1:
        characters = string.ascii_letters  # Letters only
    elif complexity == 2:
        characters = string.ascii_letters + string.digits  # Letters and digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation  # Letters, digits, and special characters
    else:
        return None  # Invalid complexity
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def password_generator():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 6 characters): "))
            if length < 6:
                print("Password length should be at least 6 characters for better security.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print("\nChoose password complexity:")
    print("1. Letters only (lowercase and uppercase)")
    print("2. Letters and digits")
    print("3. Letters, digits, and special characters")
    
    while True:
        try:
            complexity = int(input("Enter your choice (1/2/3): "))
            if complexity not in [1, 2, 3]:
                print("Invalid choice. Please choose a number between 1 and 3.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
    
    password = generate_password(length, complexity)
    
    if password:
        print(f"\nGenerated Password: {password}")
    else:
        print("Failed to generate password. Please try again.")

password_generator()