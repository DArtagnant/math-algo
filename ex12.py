from math import gcd as pgcd


class Fraction:
    def __init__(self, a:int, b:int):
        assert b != 0
        self.a = a
        self.b = b
    
    def __str__(self):
        return f"{self.a} / {self.b}"

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b
    
    def simpl(self):
        n_pgcd = pgcd(self.a, self.b)
        return Fraction(self.a//n_pgcd, self.b//n_pgcd)
    
    def inverse(self):
        return Fraction(self.b, self.a)
    
    def __neg__(self):
        return Fraction(-self.a, self.b)
    
    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b).simpl()
    
    def __add__(self, other):
        return Fraction((self.a * other.b) + (self.b * other.a), self.b * other.b).simpl()
    
    def __sub__(self, other):
        return self + -other
    
    def __float__(self):
        return self.a / self.b

if __name__  == "__main__":
    f = Fraction(1, 2)
    f2 = Fraction(3, 4)
    print(f * f2)
    print(f + f2)