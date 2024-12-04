from math import gcd as pgcd

class Fraction:
    def __init__(self, a:int, b:int):
        assert b != 0
        self.a = a
        self.b = b
    
    def __str__(self):
        return repr(self)
    
    def __repr__(self):
        return f"{self.a}/{self.b}"

    def __eq__(self, other):
        if isinstance(other, Fraction):
            self_simp = self.simpl()
            other_simp = other.simpl()
            return self_simp.a == other_simp.a and self_simp.b == other_simp.b
        if isinstance(other, int):
            if other == 0:
                return self.a == 0
        raise TypeError(f"Comparaison non supportée entre {self} et {other}")
    
    def simpl(self):
        n_pgcd = pgcd(self.a, self.b)
        return Fraction(self.a//n_pgcd, self.b//n_pgcd)
    
    def inverse(self):
        assert self.a != 0
        return Fraction(self.b, self.a)
    
    def __neg__(self):
        return Fraction(-self.a, self.b)
    
    def __mul__(self, other):
        assert isinstance(other, Fraction)
        return Fraction(self.a * other.a, self.b * other.b).simpl()
    
    def __add__(self, other):
        assert isinstance(other, Fraction)
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