def collatz(number):
    if number % 2 == 0:
        wynik = number // 2
        print(wynik)
        return number // 2
    elif number % 2 == 1:
        wynik2 = 3 * number + 1
        print(wynik2)
        return 3 * number + 1

l = int(input('podaj liczbe calkowitą: '))
while l != 1:
    l = collatz(int(l))
