class BigInt:
    __CHARACTERS = ["A", "B", "C", "D", "E", "F", "G", "H",
                    "I", "J", "K", "L", "M", "N", "O", "P",
                    "Q", "R", "S", "T", "U", "V", "W", "X",
                    "Y", "Z"]

    def __init__(self, arg1=None, arg2=None, max_digit_before_letters=100, base=10):
        self.base = base
        self.max_digit_before_letters = max_digit_before_letters

        if isinstance(arg1, BigInt):
            self.mantissa = arg1.mantissa
            self.p = arg1.p

        elif isinstance(arg1, int) and not arg2:
            self.mantissa, self.p = self.__get_mantissa_and_p_from_int(arg1)

        elif isinstance(arg1, int) and isinstance(arg2, int):
            self.mantissa = arg1
            self.p = arg2

    def __get_mantissa_and_p_from_int(self, integer):
        p = 0
        while integer > self.max_digit_before_letters:
            integer //= self.base
            p += 1
        return round(integer), p

    def __int__(self):
        return round(self.mantissa * self.base ** self.p)

    def __str__(self):
        if self.p > len(self.__CHARACTERS):
            p_copy = self.p
            count = 0
            while p_copy > len(self.__CHARACTERS):
                p_copy -= len(self.__CHARACTERS)
                count += 1

            return f"{self.mantissa}{count * self.__CHARACTERS[-1]}{self.__CHARACTERS[p_copy - 1]}"
        return f"{self.mantissa} {self.__CHARACTERS[self.p - 1]}"

    def __repr__(self):
        return self.__str__()


b1 = BigInt(25 * 10 ** 150)
b2 = BigInt(b1)
b3 = BigInt(25, 150)

print(b1, b2, b3)
print(int(b1), int(b2), int(b3), sep="\n")
