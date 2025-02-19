def add(a,b=0,c=0):
    return a+b+c
print(add(10,5,2))
print(add(10,5))
print(add(c=30,a =6))

def additem(item,l=[]):
    l.append(item)
    return(l)
l1= [1,2,3,4]
additem(5,l1)
print(l1)



