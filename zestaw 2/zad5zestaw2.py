def fun(N):
    
    while 1 > N  or  N > 2147483647:
        print("Podales argument funkcji z poza zakresu!")
        N = int(input("Podaj argument funkcji jeszcze raz: "))
        
    y = bin(N)
    x = list(y)
    x.remove('0')
    x.remove('b')
    l = len(x)
    list1 = []
    if x[l - 1] == '0':
        while x.pop() != '1':
            x.pop()
        x.append('1')

    for i in range(len(x)):
        if x[i] == '1':
            if i+1 < len(x):
                if x[i+1] == '0':
                    m = 0
                    while x[i+1+m] == '0':
                        m += 1
                    list1.append(m)

    list1.append(0)
    m = max(list1)
    return m


