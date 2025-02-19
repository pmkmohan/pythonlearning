def fun3(a,b,c):
    return a+1, b+1 , c+1
x,y,z = fun3( 10, 20, 30)
print(x,y,z)
t = fun3( 10, 20, 30)
print(t)




"""def fun2(a,b,c):
    print(a,b,c)

l1=[11,12,13]
fun2(l1[0],l1[1],l1[2])

fun2(*l1)



def fun1(*args):
    print(args)
fun1(1,2,2,3,3,3,3,3,3,1)
fun1(1,'Hello',2.5,True)

def fun1(a,b,*args):
    print(a,b,args)
fun1(1,2,2,3,3,3,3,3,3,1)
fun1(1,'Hello',2.5,True)

def fun1(args,a,b):
    print(args,a,b)
fun1(1,2,2)
fun1(1,'Hello',True)"""