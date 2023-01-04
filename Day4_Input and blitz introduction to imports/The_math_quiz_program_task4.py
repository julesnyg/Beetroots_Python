'''The math quiz program
Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong,
and then responds with a message accordingly.'''


My_question = 250*3
User_answer = input("Please answer 250*3: ")

Condition = bool(int(My_question) == int(User_answer))

if Condition is True:
    print("You re right")
else:
    print("You re wrong")