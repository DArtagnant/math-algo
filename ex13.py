from ex12 import Fraction
from math import ceil

def fibonacci(frac: Fraction):
    p = [1]
    d = frac
    while d := frac - Fraction(1, p[-1]) != Fraction(0, 1):
        p.append(ceil(d))
    print(f"1/{e} " for e in p)


if __name__ == "__main__":
    fibonacci(Fraction(1, 2))
    fibonacci(Fraction(5, 4))
    fibonacci(Fraction(-1, 2))
    fibonacci(Fraction(-5, 4))