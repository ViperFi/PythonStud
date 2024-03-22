import math

# Wczytanie liczby od użytkownika
liczba = int(input("Podaj liczbę całkowitą: "))

# Obliczenie cyfry jedności
cyfra_jednosci = abs(liczba) % 10

# Sprawdzenie parzystości liczby
parzysta = "parzystą" if liczba % 2 == 0 else "nieparzystą"

# Wyświetlenie komunikatu A
print(f"1. Podana liczba {liczba} ma cyfrę jedności {cyfra_jednosci} oraz jest liczbą {parzysta}.")

# Sprawdzenie podzielności przez 3 i 7
podzielna_przez_3 = "podzielną" if liczba % 3 == 0 else "niepodzielną"
podzielna_przez_7 = "podzielną" if liczba % 7 == 0 else "niepodzielną"

# Wyświetlenie komunikatu B
print(f"2. Podana liczba {liczba} jest liczbą {podzielna_przez_3} przez 3 oraz {podzielna_przez_7} przez 7.")

# Sprawdzenie czy liczba jest nieujemna
if liczba >= 0:
    # Obliczenie pierwiastka kwadratowego
    pierwiastek_kwadratowy = round(math.sqrt(liczba), 2)
    # Wyświetlenie komunikatu C
    print(f"3. Pierwiastek kwadratowy powyższej liczby wynosi {pierwiastek_kwadratowy}.")
else:
    # Wyświetlenie komunikatu o braku pierwiastka
    print("3. Uwaga: pierwiastek kwadratowy powyższej liczby nie istnieje.")
