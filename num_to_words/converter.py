class NumToWordsConverter:
    def __init__(self):
        self.units = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf",
                      "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize"]
        self.tens = ["", "", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante-dix",
                     "quatre-vingts", "quatre-vingt-dix"]
        self.hundreds = ["", "cent", "deux-cents", "trois-cents", "quatre-cents", "cinq-cents",
                         "six-cents", "sept-cents", "huit-cents", "neuf-cents"]

    def convert(self, num):
            if num < 0 or num > 999999:
                raise ValueError("Number out of range (0-999999)")
            
            if num == 0:
                return self.units[0]
            
            result = ""
            if num >= 1000:
                thousands = num // 1000
                result += self._convert_hundreds(thousands) + " mille"
                if thousands > 1:
                    result += "s"  # Add "s" for plural
                
                num %= 1000
                if num == 0:
                    return result
            
            result += " " if result else ""
            result += self._convert_hundreds(num)
            return result

    def _convert_hundreds(self, num):
        if num == 0:
            return ""
        elif num <= 16:
            return self.units[num]
        elif num <= 19:
            return self.tens[1] + "-" + self.units[num % 10]
        else:
            result = ""
            if num >= 100:
                result += self.units[num // 100] + "-cents"
                num %= 100
                if num == 0:
                    return result
            
            result += " " if result else ""
            if num < 20:
                result += self._convert_tens(num)
            else:
                result += self.tens[num // 10]
                if num % 10 != 0:
                    result += "-" + self.units[num % 10]
            return result

    def _convert_tens(self, num):
        if num <= 16:
            return self.units[num]
        elif num == 70:
            return "soixante-dix"
        elif num == 80:
            return "quatre-vingts"
        elif num == 90:
            return "quatre-vingt-dix"
        else:
            return self.tens[num // 10] + ("-" + self.units[num % 10] if num % 10 != 0 else "")

def main():
    """
    Entry point for the command-line interface.
    """
    import sys

    if len(sys.argv) != 2:
        print("Usage: num_to_words <number>")
        sys.exit(1)

    input_list = eval(sys.argv[1])

    try:
        converter = NumToWordsConverter()
        for num in input_list:
            result = converter.convert(num)
            print(f"{num}: {result}")
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
