# Flappy Box

**Flappy Box** is a simple and fun game inspired by the classic Flappy Bird. In this game, you control a box that must navigate through a series of pipes by flapping to stay airborne. Avoid the pipes and strive for the highest score!

## Features

- **Main Menu**: Start the game, view instructions, and see the high score.
- **Play State**: Navigate through pipes and score points. The game ends if you collide with a pipe or fall below the screen.
- **Pause Menu**: Pause the game and resume or quit.
- **Game Over Screen**: View your score and high score after losing.
- **High Score Tracking**: The highest score is saved and displayed.

## Controls

- **Spacebar**: Flap to keep the box in the air.
- **P**: Pause the game.
- **Q**: Quit the game during pause.
- **Spacebar** (in Game Over): Restart the game.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/TenEplays/Python-Projects.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd Python-Projects/Flappy-Box
    ```

3. **Install Pygame**:
    ```bash
    pip install pygame
    ```

4. **Run the game**:
    ```bash
    python flappy_box.py
    ```

## How It Works

The game is built using Python and Pygame. It features a main game loop that handles the different game states (Main Menu, Play State, Pause Menu, Game Over). The `Bird` and `Pipe` classes manage the game's physics and collision detection.

## Credits

This game was developed with the help of ChatGPT AI, which provided guidance and code examples to create a fully functional Flappy Bird clone using shapes instead of images.

## License

This project is licensed under the MIT License.
