a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

if b == 0:
    print("Nie można dzielić przez 0")
else:
    dodawanie = a + b
    odejmowanie = a - b
    mnozenie = a * b
    dzielenie = a / b
    dzielenie_calkowite = a // b
    potegowanie = a ** b

    print()
    print("Dodawanie:", dodawanie)
    print("Odejmowanie: ", odejmowanie)
    print("Mnożenie:", mnozenie)
    print("Dzielenie z resztą:", dzielenie)
    print("Dzielenie całkowite:", dzielenie_calkowite)
    print("Potęgowanie:", potegowanie)
