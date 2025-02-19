"VAriable length Arguments"
def fun1(*args):
    print(args)
fun1(10,8,12.6,'john',16)


def fun2(**kwargs):
    print(kwargs)
fun2(name='ajay',age=10,addreess = "Hyderabad")

def fun2(**kwargs):
    for x in kwargs:
        print(x,kwargs[x])

fun2(name='ajay',age=10,addreess = "Hyderabad")

def fun3(a,b,*args,**kwargs):
    print(a,b,args,kwargs)

fun3(10,20 ,15,16,17,name='ajay',age=10,addreess = "Hyderabad")