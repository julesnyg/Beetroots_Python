'''Words combination

Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
For example, the program obtained the word ‘hello’, so it should print 5 random strings(words)
that combine characters 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
Tips: Use random module to get random char from string)'''

import random


User_string = list(input("Please type something: "))

random.shuffle(User_string)

'''number of characters in the string'''
length_of_characters = len(User_string)

'''number of outputs'''
'''I chose to use 'range' function because it wont require me to increase the iteration value , after printing first result 
it suits to be used along side for loop'''
number_of_outputs = range(0,5)

'''here it start to print the result then check if the condition is verified, if yes it stops, otherwise it continues to print the result'''
for n in number_of_outputs:
    '''result'''
    print(''.join(User_string))
    '''reshuffling again for the new output'''
    random.shuffle(User_string)