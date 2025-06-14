from src.utils import choose_word, get_hangman, MAX_TRIES

class Hangman:
    def __init__(self):
        self.word = choose_word()
        self.guessed_letters = set()
        self.tries = 0

    # Get the current state of the word
    def get_word(self):
        word =  [letter if letter in self.guessed_letters else "_" for letter in self.word]
        return " ".join(word)
    
    # Get the guessed letters in alphabetical order
    def get_guessed_letters(self):
        letters = sorted(self.guessed_letters)
        return ' '.join(letters)

    # Get the number of tries left
    def get_tries_left(self):
        return MAX_TRIES - self.tries

    # Check if the game is won
    def is_won(self):
        return set(self.word).issubset(self.guessed_letters)

    # Get a guess from the player
    def get_guess(self):
        # Validate input
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Enter a valid single letter (a-z).")
                continue
            if guess in self.guessed_letters:
                print("Letter already guessed.")
                continue
            break

        # Process guess
        self.guessed_letters.add(guess)
        if guess not in self.word:
            self.tries += 1
            return f"Wrong! {self.get_tries_left()} tries left."
        return "Correct!"

    # Play the game
    def play(self):
        print("Welcome to Hangman!")

        # Choose number of players
        while True:
            try:
                numPlayers = int(input("Enter number of players (1 or 2): "))
                if not 1 <= numPlayers <= 2:
                    raise ValueError
                break
            except ValueError:
                print("Enter a valid number (1 or 2).")
                continue

        # If two players, get a word from player 1
        if numPlayers == 2:
            self.word = input("Player 1, enter a word to guess: ").lower()
            print("\n" * 50)
            print("Player 2, guess the word!")

        # Main game loop
        while self.get_tries_left() > 0:
            print(get_hangman(self.tries))
            print(self.get_word())
            if self.get_tries_left() < MAX_TRIES:
                print(f"Guessed letters: {self.get_guessed_letters()}")
            print(self.get_guess())

            # Check for win
            if self.is_won():
                print(f"You win! The word was {self.word}.")
                return
            
        # Game over
        print(get_hangman(self.tries))
        print(f"You lose! The word was {self.word}.")
        return