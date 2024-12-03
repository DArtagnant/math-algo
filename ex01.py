x = 14
y=34
z=-12
print(x % 7 == 0)

if x >= y:
    print(x % y == 0)
else:
    print(y % x == 0)

if (x >= 0 and y >=0 and z>=0 ) or (x <= 0 and y <= 0 and z<= 0) :
    print(True)
else :
    print(False)

if (x != y and z != y  and x != z):
    print(True)
else :
    print(False)
