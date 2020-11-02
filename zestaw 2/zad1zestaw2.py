list1 = [3, 4,[2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]
a = list1
i = 0
while i < len(a):
    if isinstance(a[i], list):
        a = a[i]
        i = 0
    else:
        i += 1
koniec = a[len(a)-1]
a.append(koniec + 1)
print(list1)
