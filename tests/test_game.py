import unittest
from unittest.mock import patch
from src.game import Hangman

class TestHangman(unittest.TestCase):
    # Set up a game instance with a word
    def setUp(self):
        self.game = Hangman()
        self.game.word = "apple"

    # Test get_word initial
    def test_get_word_initial(self):
        self.assertEqual(self.game.get_word(), "_ _ _ _ _")

    # Test get_word after guesses
    def test_get_word_after_guess(self):
        self.game.guessed_letters.update(['a', 'p'])
        self.assertEqual(self.game.get_word(), "a p p _ _")

    # Test get_guessed_letters
    def test_get_guessed_letters(self):
        self.game.guessed_letters.update(['b', 'a', 'c'])
        self.assertEqual(self.game.get_guessed_letters(), "a b c")

    # Test get_tries_left
    def test_get_tries_left(self):
        self.game.tries = 2
        self.assertEqual(self.game.get_tries_left(), 4)

    # Test is_won false
    def test_is_won_false(self):
        self.game.guessed_letters.update(['a', 'p'])
        self.assertFalse(self.game.is_won())

    # Test is_won true
    def test_is_won_true(self):
        self.game.guessed_letters.update(['a', 'p', 'l', 'e'])
        self.assertTrue(self.game.is_won())

    # Test get_guess correct
    @patch('builtins.input', side_effect=['a'])
    def test_get_guess_correct(self, mock_input):
        result = self.game.get_guess()
        self.assertEqual(result, "Correct!")
        self.assertIn('a', self.game.guessed_letters)

    # Test get_guess wrong
    @patch('builtins.input', side_effect=['z'])
    def test_get_guess_wrong(self, mock_input):
        tries_before = self.game.tries
        result = self.game.get_guess()
        self.assertEqual(result, f"Wrong! {self.game.get_tries_left()} tries left.")
        self.assertEqual(self.game.tries, tries_before + 1)

    # Test repeated guesses
    @patch('builtins.input', side_effect=['a', 'a', 'b'])
    def test_repeated_guess(self, mock_input):
        self.game.guessed_letters.add('a')
        result = self.game.get_guess()
        self.assertIn('b', self.game.guessed_letters)

    # Test invalid input
    @patch('builtins.input', side_effect=['1', '', 'ab', 'c'])
    def test_invalid_input(self, mock_input):
        result = self.game.get_guess()
        self.assertIn('c', self.game.guessed_letters)

    # Test game loss
    @patch('builtins.input', side_effect=['x', 'y', 'z', 'q', 'w', 't'])
    def test_game_loss(self, mock_input):
        for _ in range(self.game.get_tries_left()):
            self.game.get_guess()
        self.assertEqual(self.game.get_tries_left(), 0)
        self.assertFalse(self.game.is_won())

    # Test two player mode
    @patch('builtins.input', side_effect=['2', 'apple', 'a', 'p', 'l', 'e'])
    def test_two_player_win(self, mock_input):
        game = Hangman()
        game.play()
        self.assertTrue(game.is_won())
        self.assertEqual(game.word, "apple")

if __name__ == "__main__":
    unittest.main()