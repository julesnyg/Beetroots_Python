'''Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:

"Good day <name>! <day> is a perfect day to learn some python."
Note that <name> and <day> are predefined variables in source code.

An additional bonus will be to use different string formatting methods for constructing result string.

 '''

import datetime


'''option 1'''
name = input("Please type your name: ")
date = datetime.datetime.today()

print("Good day ", name, "!"" Today ",date, " is the perfect day to learn python")


'''option 2'''
named= input("Please type your name: ")
dated= datetime.date.today()

print("Good day ", named, "!"" Today ",dated, " is the perfect day to learn python")