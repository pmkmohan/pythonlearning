def add(a,b,c,d,e,f):
    print(a,b,c,d,e,f)
    return a+b+c+d+e+f
print(add(1,2,3,4,5,6))

def add(a,b,/,c,d,e,f):
    print(a,b,c,d,e,f)
    return a+b+c+d+e+f
print(add(1,2,3,4,5,6))

def add(a,b,/,c,d,*,e,f):
    print(a,b,c,d,e,f)
    return a+b+c+d+e+f
print(add(1,2,3,4,e=5,f=6))

def addon(*,a,b):
    print(a,b)
    return a+b
print(addon(a=5,b=6))

def addon(a,b,/):
    print(a,b)
    return a+b

addon(1,2)
