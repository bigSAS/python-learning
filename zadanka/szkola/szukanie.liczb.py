# sprawdz czy dana liczba wystepuje na liscie liczb

# uzyj petli, jesli liczba X wystepuje to wypisz "liczba X wystepuje w liscie"
# jesli nie to odwrotnie

lista_liczb = [1, 1, 12, 33, 4, -5, 6, 7, 2.32, -10, 10]

# matiks rozwiazanie

while True:  # program ma sie wykonywac dopoki nie zostanie przerwany
    znaleziono = False  # deklarujemy zmienna bool (czy znaleziono) wyjsciowo False
    x = input("Wprowadz liczbe: ")  # wczytujemy liczbe z klawiatury
    y = int(x) # zamieniamy liczbe ze str na int (wczytana z input() zawsze jest str!)
    for liczba in lista_liczb:  # iterujemy sie po liczbach w liscie
        if y == liczba:  # jesli liczba to szukana liczba
            znaleziono = True  # ustaw znaleziono na True (bo znaleziono ;))
            break  # przerwij petle (nie trzeba dalej szukac bo znaleziono)
    if znaleziono:  # sprawdzamy czy znaleziono
        print("Znaleziono liczbe")
    else:
        print('Nie znaleziono')

# ! nie potrzeba zandej petli na liscie liczb zeby sprawdzic czy lista zawiera dana liczbe

# while True:  # program ma sie wykonywac dopoki nie zostanie przerwany
#     x = int(input("wprowadz liczbe: "))  # Wczytujemy z klawiatury i zamieniamy na int
#     znaleziono = x in lista_liczb  # sprawdzamy czy lista zawiera podana liczbe
#     if znaleziono: # sprawdzamy czy znaleziono
#         print("jest :)")
#     else:
#         print("ni mo :(")


# ! 4 fun - ternary operator
# while True:
#     print("jest :)") if int(input("wprowadz liczbe: ")) in lista_liczb else print("ni mo :(")
