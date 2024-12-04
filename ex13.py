from ex12 import Fraction
from math import ceil

def egypt(frac: Fraction):
    if frac != 0:
        p = ceil(frac.inverse())
        yield p
        yield from egypt(frac - Fraction(1, p))

def egypt2(frac: Fraction):
    while frac != 0:
        p = ceil(frac.inverse())
        yield p
        frac -= Fraction(1, p)


if __name__ == "__main__":
    print(list(egypt(Fraction(25, 28))))
    print(list(egypt2(Fraction(25, 28))))