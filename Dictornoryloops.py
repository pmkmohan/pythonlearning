dictx = { 101:'John',102 :'Smith',103:'Mark',104:'David'}
for x in dictx:
    print(x)
    print(x,dictx[x])
for x in dictx:
    print(x,dictx.get(x))
print(dictx[102])
print(dictx.get(106))
print(dictx.get(101,'unknowne'))
print(dictx.keys())
print(dictx.values())
print(dictx.items())