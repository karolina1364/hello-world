X = input("podaj x: ")

while X.isdigit() != True:
    print("Nie podales liczby calkowitej dodatniej!")
    X = input("podaj x: ")

Y = input("podaj y: ")
while Y.isdigit() != True:
    print("Nie podales liczby calkowitej dodatniej!")
    Y = input("podaj y: ")

Z = input("podaj z: ")
while Z.isdigit() != True:
    print("Nie podales liczby calkowitej dodatniej!")
    Z = input("podaj z: ")

N = input("podaj n: ")
while N.isdigit() != True:
    print("Nie podales liczby calkowitej dodatniej!")
    N = input("podaj n: ")

x = int(X)
y = int(Y)
z = int(Z)
n = int(N)
list0 = []
list1 = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                pomoc = [i,j,k]
                list1.append(pomoc)

print(list1)
