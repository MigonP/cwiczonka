import random
secretNumber= random.randint(1,20)
print('Mam na myśli pewną liczbe z zakresu od 1 do 20!')

for guessesTaken in range(1, 7):
    print('Spróbuj odgadnać liczbę')
    guess= int(input())

    if guess < secretNumber:
       print('podabna liczba jest za mała')
    elif guess > secretNumber:
        print('podana liczba jest za duża')
    else:
        break

if guess == secretNumber:
    print('odgadłeś liczbe w ciagu ' + str(guessesTaken) + ' prób!' )
else:
    print('nie udalo sie. Liczba, którą mialem na mysli to ' + str(secretNumber))