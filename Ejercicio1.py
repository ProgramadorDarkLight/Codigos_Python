def max_de_tres(a,b,c):

    if a >= b and a >= c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

print(max_de_tres(10,20,15))