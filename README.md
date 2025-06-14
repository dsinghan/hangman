# Hangman

Hangman game written in Python.

## Features

- Single-player mode
- Two-player mode
- Input validation
- Tracking of guessed letters and remaining tries
- ASCII art hangman display
- Win and loss detection
- Unit tests

## Project Structure

```
hangman/
├── src/
│   ├── __main__.py
│   ├── game.py         # Game logic
│   ├── utils.py        # Utility functions
│   └── words.txt       # Word list
└── tests/
    ├── test_game.py
    └── test_utils.py
```

### Running the Game

From the project root, run:
```sh
python3 -m src
```

### Running Tests

From the project root, run:
```sh
python3 -m unittest discover tests
```

## Customizing Words

Edit `src/words.txt` to add or remove words for single-player mode.  
Each word should be on its own line.
