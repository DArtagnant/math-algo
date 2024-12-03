from decimal import Decimal, getcontext

getcontext().prec = 60

precision = 20

a = Decimal('0')
b = Decimal('2')

for k in range(precision):
    a = (2 + a)**Decimal('0.5')
    b = (2 * b) / a

print(b)