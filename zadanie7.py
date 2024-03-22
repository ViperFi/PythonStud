# Wczytanie długości i szerokości prostokąta
dlugosc = int(input("Podaj długość prostokąta: "))
szerokosc = int(input("Podaj szerokość prostokąta: "))
znak = input("Podaj znak do narysowania prostokąta: ")

# Wersja 1: Prostokąt pełny
print("Wersja 1:")
for _ in range(szerokosc):
    print(znak * dlugosc)

# Wersja 2: Prostokąt z ramką
print("\nWersja 2:")
print(znak * dlugosc)  # Górna krawędź
for _ in range(szerokosc - 2):
    print(znak + " " * (dlugosc - 2) + znak)  # Środkowe wiersze
if szerokosc > 1:
    print(znak * dlugosc)  # Dolna krawędź