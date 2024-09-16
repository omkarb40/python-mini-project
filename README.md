# Python-Based Gaming Application

Welcome to the **Python-Based Gaming Application**! This app lets you play two fun games: **Rock Paper Scissors** and **Cows and Bulls** against the computer. Dive in and enjoy the classic gaming experience!

## Features

### Main Menu
- Choose from two games: **Rock Paper Scissors** or **Cows and Bulls**.
- Option to exit the application.

### Rock Paper Scissors
- **Gameplay**: Compete against the computer to score 3 points and win.
- **User Choice**: 
  - Enter `0` for Rock.
  - Enter `1` for Paper.
  - Enter `2` for Scissors.
  - Enter `-1` to exit.
- **Rules**: 
  - Rock breaks scissors.
  - Scissors cut paper.
  - Paper covers rock.
  
### Cows and Bulls
- **Gameplay**: Guess the 4-letter word chosen by the computer.
- **Feedback**:
  - **Cows**: Number of correct letters in the wrong position.
  - **Bulls**: Number of correct letters in the correct position.
- **Rules**: The game continues until you guess correctly or you exhaust the 15 attempts.

## How to Play
1. **Run the Program**: Execute the Python script in your Python environment.
2. **Main Menu**: You’ll be presented with a menu to select the game.
3. **Choose a Game**: Follow the on-screen instructions to start playing.
4. **Exit**: You can return to the main menu or exit the game at any time.

## Game Flow

### Welcome Screen
Each game starts with a decorative welcome screen followed by the game menu.

### Main Menu
From the main menu, you can:
- Choose to play **Rock Paper Scissors** or **Cows and Bulls**.
- Exit the program.

### Rock Paper Scissors Menu
- Choose to start the game or read the rules.
- Score 3 points before the computer to win.

### Cows and Bulls Menu
- Guess the 4-letter secret word.
- Get feedback in the form of **Cows** (correct letters in wrong position) and **Bulls** (correct letters in correct position).
- Maximum of 15 guesses allowed.

## Dependencies
- This game is built using Python's standard library and requires no external dependencies.
- Python's `random` module is used for generating random choices.

## Known Issues
- The word list for **Cows and Bulls** is currently limited to 10 words. You can easily expand this by editing the `words` array in the code.
- Some parts of the code could benefit from additional input validation (e.g., non-integer inputs for menu choices).

## Future Improvements
- Adding more words to the **Cows and Bulls** word bank.
- Improving input validation for a more robust user experience.

## How to Contribute
If you have suggestions or want to contribute to this project:
1. Fork the repository.
2. Make your changes.
3. Submit a pull request for review.

---

**Enjoy playing!**
