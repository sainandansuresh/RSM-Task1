#NumberGuess
import random

num = random.randint(1, 99)
#num=int(input("Enter the number"))
guesses = 0

while guesses < 3:
    guess = int(input('Enter the number '))
    guesses += 1
    if guess < num:
        print('Sorry! Your guess is too low')
    if guess > num:
        print('Sorry! Your guess is too high')
    if guess == num:
        break

if guess == num:
    print('Yey! You guessed the correct number' + str(guesses) + ' tries!')
else:
    print('Sorry, You did not guess the number, The number was ' + str(num))
