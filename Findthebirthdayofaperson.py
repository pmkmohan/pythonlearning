birthday = {
    'Mohan':'08/09/1981',
    'UshaRani':'06/06/1987',
    'Devansh':'05/01/2017',
    'Akshya':'31/05/2021',
     }
name = str(input("Enter the Name of the persion staring with captal letter to know his birthday :"))
if name not in birthday:
    print("Not in given list")
else:
    print('Birthday of',name, 'is',birthday[name])
