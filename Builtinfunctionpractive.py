
a=abs(-2.5)
print(a)
x=ascii('0b1100')
print(x)
l = bin(12)
print(l)

L=['A','B','C','D']
e=enumerate(L)
for i in e:
    print(i)
s= 'x=10\ny=20\nprint(x+y)'
exec(s)
l1=[3,5,6,4,6,8,19,21]
print(l1)
def even(x):
    if x%2==0:
        return True
    else:
        return False
f=filter(even,l1)
for i in f:
    print(i)
print(l1)
x =filter(lambda x: x>10,l1)
for i in x:
    print(i)

s1='abcde'
print(hasattr(s1,'lower'))
print(hash(s1))
print(len(l1))
L1= [1,2,3,4,5]
L2 =[5,6,7,8,9]
print(L1,L2)
m = map(lambda x:x**2,L1)
print(list(m))
n = map(lambda x,y:x*y,L1,L2)
print(list(n))
print(max(L1))
print(min(L2))
print(sum(L1))
print(sorted(L1,reverse=True))
