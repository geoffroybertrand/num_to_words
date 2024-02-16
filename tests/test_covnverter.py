import unittest
from num_to_words.converter import NumToWordsConverter

class TestNumToWordsConverter(unittest.TestCase):
    def setUp(self):
        self.converter = NumToWordsConverter()

    def test_convert(self):
        self.assertEqual(self.converter.convert(0), "zéro")
        self.assertEqual(self.converter.convert(16), "seize")
        self.assertEqual(self.converter.convert(21), "vingt-et-un")
        self.assertEqual(self.converter.convert(38), "trente-huit")
        self.assertEqual(self.converter.convert(100), "cent")
        self.assertEqual(self.converter.convert(205), "deux-cent-cinq")
        self.assertEqual(self.converter.convert(999), "neuf-cent-quatre-vingt-dix-neuf")
        
if __name__ == '__main__':
    unittest.main()
