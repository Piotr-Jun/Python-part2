import random

def zgadywanie_liczby():
    n = random.randint(0, 100)
    liczba_gracza = int(input("Zgadnij liczbę: "))
    iteracje = 1

    while liczba_gracza != n:
        if liczba_gracza > n:
            print("Twoja liczba jest większa")
        else:
            print("Twoja liczba jest mniejsza")
        liczba_gracza = int(input("Zgadnij liczbę: "))
        iteracje += 1

    print(f"Odgadłeś liczbę {n} po {iteracje} iteracjach")

zgadywanie_liczby()