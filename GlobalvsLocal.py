g = 10
def fun1(a,b):
    c= a+b
    print('Locat',c)
    print('Global',g)

fun1(5,4)

def fun2():
    g=20
    print(g)
fun2()

def fun3():
    global g
    g = g+10
    print('Global',g)
fun3()


a,d,c,d = 11,12,33,44
def fun4():
    x,y,z=1,2,3
    print(locals())
print(globals())
fun4()
