def sprawdz_cyfre_i_parzystosc(liczba):
    # Cyfra jedności
    cyfra_jednosci = liczba % 10
    
    # Sprawdzenie czy liczba jest parzysta
    czy_parzysta = "parzysta" if liczba % 2 == 0 else "nieparzysta"
    
    # Wyświetlenie komunikatu
    print("1. Podana liczba", liczba, "ma cyfrę jedności", cyfra_jednosci, "oraz jest liczbą", czy_parzysta + ".")

def sprawdz_podzielnosc(liczba):
    # Sprawdzenie podzielności przez 3 i 7
    przez_3 = "podzielna" if liczba % 3 == 0 else "niepodzielna"
    przez_7 = "podzielna" if liczba % 7 == 0 else "niepodzielna"
    
    # Wyświetlenie komunikatu
    print("2. Podana liczba", liczba, "jest liczbą", przez_3, "przez 3 oraz", przez_7, "przez 7.")

def czy_nieujemna(liczba):
    #Sprawdzanie czy liczba jest nieujemna
    nieujemna = "nieujemna" if liczba >= 0 else "podzielna"
    #komunikat nieujemnej
    print("Podana liczba")




# Wczytanie liczby od użytkownika
liczba = int(input("Podaj liczbę całkowitą: "))

# Wywołanie funkcji sprawdz_cyfre_i_parzystosc
sprawdz_cyfre_i_parzystosc(liczba)

# Wywołanie funkcji sprawdz_podzielnosc
sprawdz_podzielnosc(liczba)
