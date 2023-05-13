'''
Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list
that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
Constraint: use only while loop for iteration.
'''


List_1 = []
List_2 = []
Num = []
List_3 = []

i = 0
while i < 101:
    if i%7 == 0:
        List_1.append(i)
    i += 1

n = 0
while n < 101:
    Num = n*5
    List_2.append(Num)
    n += 1

print(List_1)
print(List_2)

List_3 = set(List_1).difference(set(List_2))
print(list(List_3))