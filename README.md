
# Snake Game

This project is a simple implementation of the classic Snake Game, built as part of the "100 Days of Code: The Complete Python Pro Bootcamp" on Udemy. The game was developed using Python's `turtle` module, allowing players to control the snake and try to eat as much food as possible while avoiding collisions with the walls or the snake's own tail.

## Project Structure

The project consists of the following Python files:

- **main.py**: The main file that initializes the game, sets up the screen, and contains the game loop.
- **snake.py**: Defines the `Snake` class, which handles the creation, movement, and growth of the snake.
- **food.py**: Defines the `Food` class, responsible for generating food at random positions on the screen.
- **scoreboard.py**: Defines the `Scoreboard` class, which displays the player's current score and shows a "Game Over" message when the game ends.

## How to Play

- Use the arrow keys to control the snake's direction (Up, Down, Left, Right).
- The goal is to eat the blue food that appears randomly on the screen. Each time the snake eats the food, it grows longer, and the score increases.
- The game ends when the snake collides with the walls or with its own tail.

## How to Run the Game

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/snake-game.git
   cd snake-game
   ```

2. **Run the game:**

   You can run the game by executing the `main.py` file:

   ```bash
   python main.py
   ```

3. **Play the game:**

   After running the game, a window will appear where you can start playing by controlling the snake with the arrow keys.

## Key Components

### Snake

The `Snake` class is responsible for creating the snake and managing its movement. It handles the following:

- **Creating the Snake**: The snake starts with a default length of three segments.
- **Moving the Snake**: The snake moves forward automatically, and the player can change its direction using the arrow keys.
- **Growing the Snake**: When the snake eats the food, it grows by adding a new segment to its tail.

### Food

The `Food` class generates the food that the snake eats. The food is a small blue circle that appears at random positions on the screen.

### Scoreboard

The `Scoreboard` class keeps track of the player's score and displays it on the screen. It also shows a "Game Over" message when the game ends.

## Future Enhancements

- Add levels of increasing difficulty, where the snake's speed increases as the score goes up.
- Implement high score tracking.
- Improve the game's graphics and user interface.

