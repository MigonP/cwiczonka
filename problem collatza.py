def collatz(number):
    while number > 1:
        print(number, end= ' ')
        if (number % 2):
            number = 3 * number + 1
        else:
            number = number//2
    print(1, end=' ')


number = int(input('Podaj liczbe: '))
print('Wynik: ', end=' ')
collatz(number)



