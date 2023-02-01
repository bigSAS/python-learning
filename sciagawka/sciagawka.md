# Pajtong 🐍

## Typy danych i zmienne

### bool (True / False)

"prawda / fałsz"

```python
# bezpośrednia ewaluacja wyrazenia logicznego
print(1 + 1 == 2)
> True
# przypisanie do zmiennej ewaluacji wyrazenia logicznego
wynik_jest_poprawny  = 1 + 1 > 3
print(wynik_poprawny)
> False
```

negujemy poprzez uzycie `not`

```python
wynik_jest_poprawny  = 1 + 1 > 3
print(not wynik_jest_poprawny)
> True
```

### int

liczby całkowite

```python
dyszka = 10
dwie_dyszki = dyszka + 10
print(dwie_dyszki)
> 20
```
mozna uzywac `_` zeby bylo czytelniej

```python
dwajscia_kola = 20_000
print(dwajscia_kola)
> 20000
type(dwajscia_kola)
> <class:int>
```

### float

liczby zmienno przecinkowe

```python
dwa_i_pol = 2.5
cztery_i_pol = dwa_i_pol + 2
print(cztery_i_pol)
> 4.5
type(cztery_i_pol)
> <class:float>
```

### str

stringi - ciągi znaków

stringi mozna deklarowac w pojedynczych quotach `'` a takze w podwojnych `"`

```python
tworca_pythona = "guido van rossum"
print(tworca_pythona)
> guido van rossum

ala_ma = "ala ma"
kota = "kota"
ala_ma_kota = ala_ma + " " + kota.upper()
print(ala_ma_kota)
> ala ma KOTA
```
tu mozes poczytac wiecej o stringach
https://saskodzi.pl/blog/python-string-fun

### None (null)

czyli nic, glownie uzywane do sprawdzenia czy cos istnieje / nie istnieje

```python
cos = None

if cos is not None:
    print("cos istnieje")
else:
    print("cos nie istnieje")
> cos nie istnieje
```

## IF'y (instrukcje warunkowe)

stosujemy aby wywołać kawałek kodu tylko jeśli dany warunek logiczny jest spełniony

```python
pada_snieg = True

if pada_snieg:
    print("Pada snieg")
else:
    print("Nie pada snieg")
```

mozemy zagniezdzic logike

```python
pada_snieg = True
ilosc_sniegu_cm = 10
if pada_snieg:
    print("Pada snieg")
    if ilosc_sniegu_cm > 5 and ilosc_sniegu <= 10:
        print("mozemy lepij balwana")
    elif ilosc_sniegu > 10:
        print("za duzo sniegu na lepienie balwana")
    else:
        print("za malo sniegu na lepienie balwana")
```

## Pętle (for, while)

### while

petla while wykonuje sie dopoki jej warunek jest `True`

```python
licznik = 0

while licznik < 3:
    print(licznik)
    licznik = licznik + 1
> 0
> 1
> 2
```

nieskonczona petla while

```python
while True:
    print("bez konca...")
> bez konca...
> bez konca...
> bez konca...
... ;)
```

### for

zawsze skonczona petla, wykona sie tyle razy ile elementow w liscie ktora przetwarza

```python
liczby = range(10)

for i in liczby:
    print(i)
> 0
> 1
> 2


zwierzaki = ["kot", "pies", "aligator"]
for zwierze in zwierzaki:
    print(zwierze)
> kot
> pies
> aligator
```

jesli potrzebujemy indeksu aktualnego elementu w petli uzywamy funkcji `enumerate`

```python
for i, zwierze in enumerate(zwierzaki):
    print(i, zwierze)
> 0 kot
> 1 pies
> 2 aligator
```

## Listy (tablice)

Lista to zbior (kolekcja) elementow (obiektow)

deklarujemy ja uzywajac nawiasow `[]`

```python
zwierzaki = ["kot", "pies", "aligator"]
print(zwierzaki)
> ['kot', 'pies', 'aligator']
```

mozemy odniesc sie do elementu po indeksie (indeksy zawsze zaczynaja sie od zera ☝🏼)

```python
print(zwierzaki[0])
> kot
print(zwierzaki[2])
> aligator
```

jesli chcemy dodac element do listy uzywamy `<lista>.append(<element>)`

```python
zwierzaki.append("ptak")
print(zwierzaki)
> ['kot', 'pies', 'aligator', 'ptak']
```

## Słowniki

https://saskodzi.pl/blog/python-dictionary-fun - dla zajawki 👀
