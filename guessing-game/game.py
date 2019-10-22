"""A number-guessing game."""
from random import randint

greet = "Hello there."

print(greet)

name = input("What's your name? ")

print("{}, I'm thinking of a number between 1 and 100".format(name))

num = randint(1, 100)

def guessing_game(num):
    guesses = 1
    while True:
        guess = int(input("What do you think the number is? "))
        
        if guess < num:
            print("Your guess is too low, try again.")
            guesses += 1
        
        elif guess > num: 
            print("Your guess is too high, try again")
            guesses += 1
        
        else:
            print("Great job, {}! You guessed the number in {} tries!".format(name, guesses))
    
            return


guessing_game(num)

