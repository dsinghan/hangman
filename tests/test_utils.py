import unittest
from src import utils

class TestUtils(unittest.TestCase):
    # Test choose_word
    def test_choose_word_returns_word(self):
        word = utils.choose_word()
        self.assertIsInstance(word, str)
        self.assertGreater(len(word), 0)

    # Test get_hangman
    def test_get_hangman_returns_phase(self):
        for i in range(len(utils.PHASES)):
            phase = utils.PHASES[i]
            self.assertIsInstance(phase, str)
            self.assertIn("+---+", phase)

if __name__ == "__main__":
    unittest.main()