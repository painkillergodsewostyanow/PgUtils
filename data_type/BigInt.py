from __future__ import annotations
import sys


class BigInt:
    __CHARACTERS = ["A", "B", "C", "D", "E", "F", "G", "H",
                    "I", "J", "K", "L", "M", "N", "O", "P",
                    "Q", "R", "S", "T", "U", "V", "W", "X",
                    "Y", "Z"]

    def __init__(

            self,
            arg1: int | float | BigInt = None,
            arg2: int = None,
            max_digit_before_letters: int = 100,
            base: int = 1000

    ):

        self.base: int = base
        self.max_digit_before_letters: int = max_digit_before_letters
        self.mantissa: int | float
        self.p: int

        if isinstance(arg1, BigInt):
            self.mantissa = arg1.mantissa
            self.p = arg1.p

        elif isinstance(arg1, int) and not arg2:
            self.mantissa, self.p = self.__get_mantissa_and_p_from_int(arg1)

        elif isinstance(arg1, float) and isinstance(arg2, int):
            self.mantissa = arg1
            self.p = arg2

        self.__update()

    def __get_mantissa_and_p_from_int(self, integer: int) -> (float, int):
        p = 0
        while integer > self.max_digit_before_letters:
            integer /= self.base
            p += 1
        return integer, p

    def __update(self) -> None:
        while self.mantissa >= self.max_digit_before_letters:
            self.mantissa /= self.base
            self.p += 1

    def __inc_power(self, p: int) -> BigInt:
        result = BigInt(self.mantissa, self.p)
        while result.p < p:
            result.mantissa /= self.base
            result.p += 1
        return result

    def __copy__(self) -> BigInt:
        return BigInt(self.mantissa, self.p)

    def __add__(self, other: BigInt | int) -> BigInt:
        if not isinstance(other, BigInt):
            if not isinstance(other, int):
                raise ValueError

            other = BigInt(other)

        max_power = max(self.p, other.p)
        val1 = self.__copy__().__inc_power(max_power)
        val2 = other.__copy__().__inc_power(max_power)
        return BigInt(val1.mantissa + val2.mantissa, max_power)

    def __radd__(self, other: BigInt | int) -> BigInt:
        return self + other

    def __int__(self) -> int:
        return round(self.mantissa * self.base ** self.p)

    def __str__(self):
        if self.p > len(self.__CHARACTERS):
            p_copy = self.p
            count = 0
            while p_copy > len(self.__CHARACTERS):
                p_copy -= len(self.__CHARACTERS)
                count += 1

            if p_copy > 0:
                return f"{self.mantissa:.1f}{count * self.__CHARACTERS[-1]}{self.__CHARACTERS[p_copy - 1]}"
            return f"{self.mantissa:.1f}{count * self.__CHARACTERS[-1]}"

        if self.p > 0:
            return f"{self.mantissa:.1f} {self.__CHARACTERS[self.p - 1]}"
        return f"{self.mantissa:.1f}"

    def __repr__(self):
        return f"{self.__class__.__name__}: (mantissa: {self.mantissa}, power: {self.p})"

    def __mul__(self, other: int | float | BigInt) -> BigInt:

        if isinstance(other, BigInt):
            other = other.mantissa

        result = BigInt(self.mantissa * other, self.p)
        return result

    def __rmul__(self, other: int | float | BigInt) -> BigInt:
        return self * other


a = BigInt(5000)

print(int(a))

for _ in range(100):
    a += 10
print(int(a))

a *= 10

print(int(a))
