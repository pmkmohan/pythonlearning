### Differenc Between Two Number
###check if maximum difference between them is 5. if so print True else False.
a= int(input('Give first number'))
b =int(input("Give second number"))
c= a-b
print('Differenc is',abs(c))
if round(c) <= 5:
    print ("As difference is less than or equal to 5",True)
else:
    print ("As difference is greater than 5",False)


