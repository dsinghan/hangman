import random

#Choose random word from word list
def choose_word():
    with open("src/words.txt", "r") as file:
        words = file.read().splitlines()
    return random.choice(words).lower()

PHASES = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

# Get hangman phase from number of tries
def get_hangman(tries):
    return PHASES[tries]

MAX_TRIES = len(PHASES) - 1