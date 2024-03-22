import ctypes

print("Podaj następujące dane studenta:")
imie = input("- imie:")
nazwisko = input("- nazwisko:")
nr_albumu = input("- nr albumu:")

if not nr_albumu.isdigit():
    print("Uwaga: niepoprawny numer albumu!")
    exit()

punkty = float(input("- punkty:"))

inicjal = (nazwisko[0] + imie[0] + nr_albumu).upper()

progi_ocen = {
    25: 2.0,
    30: 3.0,
    35: 3.5,
    40: 4.0,
    45: 4.5,
    50: 5.0
}

ocena = None
for prog, ocena_w in progi_ocen.items():
    if punkty <= prog:
        ocena = ocena_w
        break

if ocena is not None:
    print("Student(ka)", inicjal, "uzyskał(a)", punkty, "pkt." "co oznacza", ocena)
else:
    print("Punkty są poza zakresem.")