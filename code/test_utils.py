import unittest
from utils import unkify

class TestUtils(unittest.TestCase):

    def test_all_in_vocab(self):
        self.assertEqual(unkify("hello world", ["hello", "world"]), "hello world")

    def test_some_in_vocab(self):
        self.assertEqual(unkify("hello world", ["hello"]), "hello *UNK*")

    def test_none_in_vocab(self):
        self.assertEqual(unkify("hello world", ["foo", "bar"]), "*UNK* *UNK*")

    def test_empty_string(self):
        self.assertEqual(unkify("", ["hello"]), "")

    def test_empty_vocab(self):
        self.assertEqual(unkify("hello world", []), "*UNK* *UNK*")

    def test_multiple_spaces(self):
        # split() without arguments splits by any whitespace and discards empty strings
        # so "hello   world" becomes ["hello", "world"]
        self.assertEqual(unkify("hello   world", ["hello", "world"]), "hello world")

    def test_case_sensitivity(self):
        # Test that it is case sensitive
        self.assertEqual(unkify("Hello world", ["hello", "world"]), "*UNK* world")

    def test_punctuation(self):
        # Test that punctuation attached to words makes them unknown if not in vocab
        self.assertEqual(unkify("hello, world!", ["hello", "world"]), "*UNK* *UNK*")

if __name__ == '__main__':
    unittest.main()
