def planetid(id):
    planets={1:'Mercury',2:'Venus',3:'Earth',4:'Mars',5:'Jupiter',6:'Saturn',7:'Uranus',8:'Neptune',9:'Pluto'}
    print(planets)
    if id<=9:
        return planets[id]
    else:
        print("It is not valied id of the planet. give Id with in 1 to 9")

id = int(input("Enter the Planet Id is:"))
p = planetid(id)
print("Planet name is:", p)
