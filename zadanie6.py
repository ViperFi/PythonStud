# Wczytanie wysokości trójkąta
h = int(input("Podaj wysokość trójkąta (do 50): "))
znak = input("Podaj znak do narysowania trójkąta: ")

# Sprawdzenie czy podany znak jest pojedynczym znakiem
if len(znak) != 1:
    print("To nie jest pojedynczy znak!")
else:
    # Rysowanie trójkąta
    for i in range(1, h + 1):
        print(znak * i)