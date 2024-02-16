import unittest
from num_to_words.converter import NumToWordsConverter

class TestNumToWordsConverter(unittest.TestCase):
    def setUp(self):
        self.converter = NumToWordsConverter()

    def test_convert(self):
        self.assertEqual(self.converter.convert(0), "zéro")
        self.assertEqual(self.converter.convert(999999), "neuf-cents quatre-vingt-dix-neuf milles neuf-cents quatre-vingt-dix-neuff")
        
if __name__ == '__main__':
    unittest.main()
