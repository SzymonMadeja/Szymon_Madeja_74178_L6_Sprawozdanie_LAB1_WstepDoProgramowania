import random # Importowanie biblioteki "math" w celu użycia funkcji random.randint()

droga = random.randint(1, 10000) # Używamy funkcji random.randint() aby wylosować liczbę spośród podanego zakresu
srednie_spalanie = float(input("Podaj średnie spalanie samochodu (L/100km): ")) # Używamy funkcji float() aby móc operować na podanycb liczbach oraz aby mogły być one zmiennoprzecinkowe. Używamy funkcji input() aby użytkownik mógł wprowadzić spalanie samochodu do zmiennej
cena_paliwa = float(input("Podaj cenę paliwa (zł/l): ")) # Używamy funkcji input() aby użytkownik mógł wprowadzić cenę paliwa do zmiennej
spalanie = round(droga * (srednie_spalanie / 100),2) # Obliczenie spalania samochodu. Używamy funkcji round() aby zaokrąglić wynik do 2 miejsc po przecinku
koszt_podrozy = round(spalanie * cena_paliwa,2) # Obliczenie kosztu podróży. Używamy funkcji round() aby zaokrąglić wynik do 2 miejsc po przecinku

print("Samochód spali:",spalanie,"litrów paliwa na drodze",droga,"a koszt podróży wynosi:",koszt_podrozy,"zł") # Wypisanie tekstu z użyciem zmiennych