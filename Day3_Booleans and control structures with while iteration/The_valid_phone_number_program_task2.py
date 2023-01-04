'''The valid phone number program.

Make a program that checks if a string is in the right format for a phone number.
The program should check that the string contains only numerical characters and is only 10 characters long.
Print a suitable message depending on the outcome of the string evaluation.'''


Phone_number= input("Please type the phone number: ")

Phone_number_length= len(Phone_number)

the_number_Phone_number = bool (Phone_number.isdigit())

'''Check the length of the phone number'''
if Phone_number_length != 10:
    print("The Phone number has to be 10 digits")
else:

    '''Check_the_number Phone_number'''
    if the_number_Phone_number is False:
     print("The phone number has to be only numbers")

    else:
        print(Phone_number, " is a valid phone number")