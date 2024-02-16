class NumToWordsConverter:
    def __init__(self):
        self.units = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf",
                      "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize"]
        self.tens = ["", "", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante-dix",
                     "quatre-vingts", "quatre-vingt-dix"]
        self.hundreds = ["", "cent", "deux-cents", "trois-cents", "quatre-cents", "cinq-cents",
                         "six-cents", "sept-cents", "huit-cents", "neuf-cents"]

    def convert(self, num):
        if num < 0 or num > 999:
            raise ValueError("Number out of range (0-999)")
        
        if num <= 16:
            return self.units[num]
        
        if num <= 19:
            return self.tens[1] + "-" + self.units[num % 10]
        
        if num < 100:
            return self.tens[num // 10] + ("-" + self.units[num % 10] if num % 10 != 0 else "")
        
        if num < 1000:
            result = self.hundreds[num // 100]
            remainder = num % 100
            if remainder != 0:
                result += "-" + self.convert(remainder)
            return result

def main():
    """
    Entry point for the command-line interface.
    """
    import sys

    if len(sys.argv) != 2:
        print("Usage: num_to_words <number>")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        converter = NumToWordsConverter()
        result = converter.convert(num)
        print(result)
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()