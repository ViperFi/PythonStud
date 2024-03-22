# Wczytanie liczby n od użytkownika
n = int(input("Podaj liczbę naturalną n: "))

# Inicjalizacja zmiennej przechowującej sumę kwadratów
suma_kwadratow = 0

# Obliczenie sumy kwadratów
for i in range(1, n + 1):
    suma_kwadratow += i ** 2

# Wyświetlenie wyniku
print(f"Suma kwadratów kolejnych {n} liczb naturalnych wynosi {suma_kwadratow}.")