dict1={
    'piece':"portion of a object or of material,produced by cutting",
    'path':'a piece of cloth or other material used to mend or strengthen a torn or weak point',
    'area':'a region or part of a town,a country,or the world',
    'visit':'go to sec and spend time with(someone)',
    'with':'having or prossessing',
    'small':'less than normal'
}
print(dict1)

keys = list(dict1.keys())
values = list(dict1.values())
lens = [len(x) for x in values]


max_len = max(lens)
min_len = min(lens)

max_index = lens.index(max_len)
min_index = lens.index(min_len)

print("Max",keys[max_index], values[max_index])
print("Min",keys[min_index], values[min_index])