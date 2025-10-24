a = float(input("Podaj długość boku a: ")) # Używamy funkcji float() aby móc operować na podanych liczbach (dodawać/mnożyć) oraz aby mogły być one zmiennoprzecinkowe
b = float(input("Podaj długość boku b: ")) # Używamy funkcji float() aby móc operować na podanych liczbach (dodawać/mnożyć) oraz aby mogły być one zmiennoprzecinkowe

pole = a * b # Przypisanie do zmiennej "pole" wyniku równania "a * b"
obwod = (2 * a) + (2 * b) # Przypisanie do zmiennej "pole" wyniku równania "(2 * a) + (2 * b)"

print("Pole tego prostokąta wynosi",pole ,"cm kwadratowych a obwód",obwod,"cm") # Napisanie tekstu z użyciem powyższych zmiennych