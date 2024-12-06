from ex16a import Poly

poly = Poly([2, 1, 8, 9999999, 77])
x = 123456789
resultat = 0
for e in reversed(poly[1:]):
    resultat = x * (e + resultat)
resultat += poly[0]
    
print(resultat)
print(poly.eval(x))