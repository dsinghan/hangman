from src.utils import choose_word, get_hangman, MAX_TRIES

class Hangman:
    def __init__(self):
        self.word = choose_word()
        self.guessed_letters = set()
        self.tries = 0

    def get_word(self):
        word =  [letter if letter in self.guessed_letters else "_" for letter in self.word]
        return " ".join(word)
    
    def get_guessed_letters(self):
        letters = sorted(self.guessed_letters)
        return ' '.join(letters)

    def get_tries_left(self):
        return MAX_TRIES - self.tries

    def is_won(self):
        return set(self.word).issubset(self.guessed_letters)

    def get_guess(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            if guess in self.guessed_letters:
                print("Letter already guessed.")
                continue
            break
        self.guessed_letters.add(guess)
        if guess not in self.word:
            self.tries += 1
            return f"Wrong! Tries left: {self.get_tries_left()}"
        return "Correct!"

    def play(self):
        print("Welcome to Hangman!")
        while self.get_tries_left() > 0:
            print(get_hangman(self.tries))
            print(self.get_word())
            print(f"Guessed letters: {self.get_guessed_letters()}")
            print(self.get_guess())
            if self.is_won():
                print("Congratulations! You won!")
                return
        print(get_hangman(self.tries))
        print(f"Game over! The word was: {self.word}")
        return