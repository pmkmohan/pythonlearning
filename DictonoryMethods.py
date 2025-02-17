dict1 = {101:'Production',102:'Account',103:'Sales & Marketing',104:'Inventory'}
print(dict1)
dict2= dict1.copy()
print(dict2)
dict2[102]= 'Designing'
print(dict2)
print(id(dict1[102]))
print(id(dict2[102]))
print(id(dict1[101]))
print(id(dict2[101]))
dict1.update({105:'Design',106:'packaging'})
print(dict1)
print(dict.get(102))

