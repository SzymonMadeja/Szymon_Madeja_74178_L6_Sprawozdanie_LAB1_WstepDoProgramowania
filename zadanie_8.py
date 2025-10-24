from math import sqrt

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

if a == 0:
    print("a nie może być 0")
else:
    delta = (b ** 2) - (4 * a * c)
    if delta == 0:
        x_zero = (b * -1) / (2 * a)
        print(f"X0 = {x_zero}")
    else:
        if delta > 0:
            pierwiastek_z_delty = sqrt(delta)
            x_jeden = round(((b * -1) + pierwiastek_z_delty) / (2 * a),2)
            x_dwa = round(((b * -1) - pierwiastek_z_delty) / (2 * a),2)
            print(f"x1 = {x_jeden} x2 = {x_dwa}")
        else:
            print("Równanie sprzeczne - Brak rozwiązań")
