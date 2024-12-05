import time

# Pet class to encapsulate pet behavior and attributes
class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.hunger = 50

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 10
            self.happiness -= 5
            print(f"You fed {self.name}. Hunger decreased, but happiness slightly decreased.")
        else:
            print(f"{self.name} is not hungry!")
        self.status()

    def play(self):
        if self.happiness < 100:
            self.happiness += 10
            self.hunger += 5
            print(f"You played with {self.name}. Happiness increased, but hunger slightly increased.")
        else:
            print(f"{self.name} is already very happy!")
        self.status()

    def status(self):
        print(f"{self.name}'s Status:")
        print(f"Happiness: {self.happiness}")
        print(f"Hunger: {self.hunger}")

    def auto_update(self):
        self.hunger += 5
        self.happiness -= 5
        if self.hunger > 80:
            self.happiness -= 10
            print(f"Warning: {self.name} is very hungry! Happiness is decreasing.")

    def is_game_over(self):
        if self.hunger >= 100:
            print(f"Game Over: {self.name} became too hungry and left you...")
            return True
        if self.happiness <= 0:
            print(f"Game Over: {self.name} became too sad and ran away...")
            return True
        return False


def main():
    print("Welcome to the Virtual Pet Simulator!")
    pet_name = input("What would you like to name your pet? ")
    pet = Pet(pet_name)
    print(f"Say hello to {pet.name}! Take good care of them.")

    actions = 0
    while True:
        print("What would you like to do?")
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Check your pet's status")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.status()
        elif choice == "4":
            print(f"Goodbye! {pet.name} will miss you!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

        actions += 1
        if actions % 3 == 0:  # Automatic changes after every 3 actions
            pet.auto_update()

        if pet.is_game_over():
            break


if __name__ == "__main__":
    main()
