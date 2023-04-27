
rok_obecny = 2023
birthdate = int(input("Podaj rok urodzenia: "))
age = rok_obecny - birthdate
if age >= 18:
    print("Jesteś pełnoletni!")
else:
    print("Nie jesteś pełnoletni.")
