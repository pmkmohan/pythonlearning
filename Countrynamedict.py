countries = {}

for i in range(5):
    name = input("Enter the County name")
    if name[0].upper() not in countries:
        countries[name[0].upper()] = [name]
    else:
        countries[name[0].upper()].append(name)
print(countries)
