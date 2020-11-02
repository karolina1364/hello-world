def przestepny():
    Rok = input("Podaj rok: ")

    while int(Rok) < 1900 or int(Rok) > 100000:
        print("Podales rok z poza zakresu!")
        Rok = input("Podaj rok: ")

    rok = int(Rok)
    if rok % 4 == 0:
        if rok % 100 == 0:
            if rok % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if przestepny():
    print('Rok przestępny!')
else:
    print('Rok nie przestępny!')



