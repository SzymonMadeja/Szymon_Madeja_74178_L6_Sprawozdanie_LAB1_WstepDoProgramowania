droga = float(input("Podaj przebyty dystans: ")) # Używamy funkcji float() aby móc operować na podanycb liczbach (dodawać/mnożyć/dzielić) oraz aby mogły być one zmiennoprzecinkowe
srednie_spalanie = float(input("Podaj średnie spalanie samochodu (w litrach na 100km): ")) # Używamy funkcji float() aby móc operować na podanycb liczbach (dodawać/mnożyć/dzielić) oraz aby mogły być one zmiennoprzecinkowe
cena_paliwa = 6.5 # Przypisanie do zmiennej "cena_paliwa" liczby "6.5"
spalanie = round(srednie_spalanie * (droga / 100),2) # Obliczenie spalania samochodu
koszt_podrozy = round(spalanie * cena_paliwa,2) # Obliczenie kosztu podróży

print("Samochód spali:",spalanie,"litrów paliwa a koszt podróży wynosi:",koszt_podrozy,"zł") # Wypisanie tekstu z użyciem zmiennych