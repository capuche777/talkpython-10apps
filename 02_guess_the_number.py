import random

print('-------------------------')
print('  GUESS THE NUMBER GAME  ')
print('-------------------------')
print('')

the_number = random.randint(0, 100)
guess = -1
name = input('What is your name: ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry {0} your guess of {1} was too LOW.'.format(name, guess))
    elif guess > the_number:
        print('Sorry {0} your guess of {1} was too HIGH.'.format(name, guess))
    else:
        print('Excellent {0}, the number was {1}'.format(name, the_number))
