napis = "aaaaaa 56 ... bbb "
x = napis.split()
i = 0
for item in x:
    for c in item:
        if c.isalnum():
            i += 1
            break
print("Liczba slow: ", i)
j = 0
for item in x:
    for c in item:
        if c.isalpha():
            j += 1
print("Liczba liter: ", j)
y = list(napis)
zbior = set(y)

print("Literka ilosc")
for item in zbior:
    if item.isalpha():
        print(item,"\t\t", y.count(item))
