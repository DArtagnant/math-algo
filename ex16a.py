from itertools import zip_longest

class Poly(list):
    def __init__(self, from_list=None):
        super().__init__(self)
        if from_list is not None:
            self.extend(from_list)
        self.simpl()
    
    def simpl(self):
        while self[-1] == 0:
            del self[-1]
        return self
    
    def __add__(self, other):
        assert isinstance(other, Poly)
        return Poly([sum(e) for e in zip_longest(self, other, fillvalue=0)])

    def eval(self, x):
        return sum(e*(x**n) for n, e in enumerate(self))
    
    def __mul__(self, other):
        assert isinstance(other, Poly)
        npoly = [0]*(len(self)+len(other)-1)
        for n1, e1 in enumerate(self):
            for n2, e2 in enumerate(other):
                npoly[n1+n2] += e1 * e2

        return Poly(npoly)
    
if __name__ == "__main__":
    p1 = Poly([1, 2, 3])
    p2 = Poly([4000, 2])
    print(p1 + p2)
    print((p1 * p2).eval(2))
    print(p1.eval(2)*p2.eval(2))