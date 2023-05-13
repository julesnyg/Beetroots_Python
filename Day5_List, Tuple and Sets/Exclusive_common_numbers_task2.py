'''
Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing
the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers
'''

import random

List_1 = []
List_2 = []
List_3 = []

i = 0

while i in range(10):
    Number = random.randint(1, 10)
    List_1.append(Number)
    i = i+1

n = 0
while n in range(10):
    Number_2 = random.randint(1,10)
    List_2.append(Number_2)
    n=n+1


print(List_1)
print(List_2)

'''approach to change the lists to sets so that I can use 'intersection' function
   then change sets back to list and print the elements'''

List_3 = set(List_1).intersection(set(List_2))
print(list(List_3))

'''I would also use another approach to change the list into dict and back'''

List_33 = []

for element in List_2:
    if element in List_1:
        List_33.append(element)

print(list(dict.fromkeys(List_33)))