'''
The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers
'''

import random

Numbers = []

i=0
while i < 10:
    Random_int = random.randint(0, 10)
    Numbers.append(Random_int)
    i = i+1

print(max(Numbers))