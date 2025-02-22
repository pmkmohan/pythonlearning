def max3(a,b,c):
    print('a', a, 'b', b, 'c', c)
    if a>b and a>c:
        return a
    else:
        if b>c:
            return b
        else:
            return c

print('Max of mumber is ', max3(2,20,4))
