class BigInt:

    LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H",
               "I", "J", "K", "L", "M", "N", "O", "P",
               "Q", "R", "S", "T", "U", "V", "W", "X",
               "Y", "Z"]

    def __init__(self, arg1=None, arg2=None, max_digit_before_letters=100):

        self.max_digit_before_letters = max_digit_before_letters

        if isinstance(arg1, BigInt):
            self.mantissa = arg1.mantissa
            self.p = arg1.p

        elif isinstance(arg1, int) and not arg2:
            self.mantissa, self.p = self.get_mantissa_and_p_from_int(arg1)

        elif isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
            self.mantissa = arg1
            self.p = arg2

    def get_mantissa_and_p_from_int(self, integer):
        p = 0
        while integer > self.max_digit_before_letters:
            integer //= 10
            p += 1

        mantissa = round(integer)
        return mantissa, p

    def __int__(self):
        return round(self.mantissa * 10 ** self.p)

    def __str__(self):
        if self.p > 26:
            p_copy = self.p
            count = 0
            while p_copy > 26:
                count += 1
                p_copy -= 26

            return f"{self.mantissa}{count * 'Z'}{self.LETTERS[p_copy-1]}"
        return f"{self.mantissa} {self.LETTERS[self.p-1]}"


b1 = BigInt(25 * 10 ** 11)
b2 = BigInt(b1)
b3 = BigInt(25, 11)

print(b1, b2, b3)
print(int(b1), int(b2), int(b3), sep="\n")
