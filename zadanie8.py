# Wczytanie zakresu, początku i kroku
poczatek = int(input("Podaj początek zakresu: "))
koniec = int(input("Podaj koniec zakresu: "))
krok = int(input("Podaj krok: "))

# Wyświetlenie nagłówków
print(f"{'Liczba':<4}{'Kwadrat':<6}{'Sześcian':<8}")

# Wyświetlenie kwadratów i sześcianów
for i in range(poczatek, koniec + 1, krok):
    kwadrat = i ** 2
    szescian = i ** 3
    print(f"{i:<4}{kwadrat:<6}{szescian:<8}")