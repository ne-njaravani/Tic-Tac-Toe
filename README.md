# Tic-Tac-Toe

A classic Tic-Tac-Toe game implemented in Python with both CLI and GUI modes.

## Features

- **GUI Mode**: Beautiful graphical interface using Pygame
  - Player vs Player mode
  - Player vs Computer mode (AI opponent using minimax algorithm)
  - Interactive click-to-play gameplay
  - Visual feedback and game status display
  - Restart and menu navigation

- **CLI Mode**: Traditional text-based interface
  - Two-player local gameplay
  - Simple number-based input (1-9)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ne-njaravani/Tic-Tac-Toe.git
cd Tic-Tac-Toe
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the game:
```bash
python main.py
```

You'll be prompted to choose between:
1. **GUI Mode** - Graphical interface with single-player option
2. **CLI Mode** - Text-based two-player mode

### GUI Mode Controls
- Click on any empty square to make your move
- Use the "Restart" button to start a new game
- Use the "Main Menu" button to return to mode selection

### CLI Mode Controls
- Enter a number from 1-9 to place your mark
- Board positions:
  ```
  1 | 2 | 3
  ---------
  4 | 5 | 6
  ---------
  7 | 8 | 9
  ```

## Project Structure

- `main.py` - Entry point with mode selection
- `gui.py` - Pygame GUI implementation
- `game_logic.py` - Core game engine (used by both CLI and GUI)
- `ai_player.py` - AI opponent using minimax algorithm
- `requirements.txt` - Project dependencies

## Requirements

- Python 3.6+
- Pygame 2.5.2+

## AI Strategy

The AI player uses the minimax algorithm to calculate the optimal move for every game state, making it unbeatable when playing optimally.