class RomanConverter:
    def __init__(self):
        self.numbers = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        self.roman_strings = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        self.roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
    def roman_to_int(self, string: str) -> int:
            total = 0
            previous_number = 0
            for i in reversed(string):
                current_number = self.roman_dict.get(i)
                if current_number < previous_number:
                    total -= current_number
                else:
                    total += current_number
                previous_number = current_number
            return total
    def int_to_roman(self, integer: int) -> str:
        roman_string = ""
        i = 0
        while integer != 0:
            for num in range(integer//self.numbers[i]):
                if self.numbers[i] <= integer:
                    roman_string += self.roman_strings[i]
                    integer -= self.numbers[i]
            i += 1
        return roman_string
    
n = input().strip()
x = n[:n.index("+")]
y = n[n.index("+")+1:]
converter = RomanConverter()
z = converter.roman_to_int(x) + converter.roman_to_int(y)
print(f"{x} = {converter.roman_to_int(x)}, {y} = {converter.roman_to_int(y)}")
print(f"{x} + {y} = {converter.int_to_roman(z)}, {converter.int_to_roman(z)} = {z}")