def max2(x,y):
    if x<y:
        return y
    else:
        return x
    

max2 = lambda x, y: x if x>= y else y

def max2(x,y,z):
    if x<z and y<z :
        return z
    elif x<y and z<y:
        return y
    elif y<x and z<x:
        return x
    else:
        return x