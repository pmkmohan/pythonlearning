def Days():
    l = ['sun','mon','tue','wed','thru','fri','sat']
    i = 0
    while True:
        x = l[i]
        i = (i+1)%7
        yield x
d = Days()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))

