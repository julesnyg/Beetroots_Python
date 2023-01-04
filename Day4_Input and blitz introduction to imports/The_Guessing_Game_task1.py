'''The Guessing Game.
Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement.'''

import random


'''generating random numbers'''
numbers = (random.randint(1,10))

'''asking the user to pick a number'''
user_choice = input("Please guess the number generated: ")

'''computer generated number'''
print(numbers)


if int(user_choice) != numbers:
    print("You are wrong")
else:
    print("You are correct")