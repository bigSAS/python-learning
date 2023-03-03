"""
Napisz program do notatek
Nalezy moc:
* dodac notatke (tytul, tresc)
* zlistowac notatki ponumerowane od 1 (tytuly)
* wyswietlic szczegoly wybranej notatki po numerze (tytul i tresc)
** usunac notatke po numerze
*** usunac notatke z potwierdzeniem ze napewno chce usunac (po numerze)

Uzyj wlasnych funckji do obsluzenia 1-5
"""

komunikat_glowny = """
    Co chcesz zrobic?
    1. Dodaj notatke
    2. Listuj notatki
    3. Wyswietl szczegoly notatki
    4. Usun notatke
    5. Usun notatke z potwierdzeniem
    6. Zamknij program
"""
wybor = ""

NOTATKI = []


def sprawdz_wybor(w):
    print("\n" * 10)
    print("Wybrales", w)
    if w not in ["1", "2", "3", "4", "5", "6"]:
        print("Wybierz inna opcje niz", w, "!!!")


if __name__ == "__main__":
    while True:
        wybor = input(komunikat_glowny)
        sprawdz_wybor(wybor)
        if wybor == "6":
            break

    print("Bye! 🏀")
