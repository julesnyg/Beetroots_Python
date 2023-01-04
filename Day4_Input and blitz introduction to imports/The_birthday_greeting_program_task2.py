'''The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:
"Hello <name>, on your next birthday you’ll be <age+1> years"'''

name = input("Please type your name: ")
age = int(input("Please type your age: "))

'''out put'''
print("Hello ", name+ ' ' + "on your next birthday you'll be ", age + 1)