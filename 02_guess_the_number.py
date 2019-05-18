import random # Importa libreria para generar numeros random

print('-------------------------')
print('  GUESS THE NUMBER GAME  ')
print('-------------------------')
print()

the_number = random.randint(0, 100) # randinit genera un entero random, en este cao el rango es de 0 a 100
guess = -1
name = input('What is your name: ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print(f'Sorry {name} your guess of {guess} was too LOW.')
    elif guess > the_number:
        print(f'Sorry {name} your guess of {guess} was too HIGH.')
    else:
        print(f'Excellent {name}, the number was {the_number}')

print('Done')
