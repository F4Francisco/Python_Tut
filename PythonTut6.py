# List

import random
import math

'''
#[0 : "string"][1:1.1234][2:28][3:"c]

randlist = ["string", 1.234, 28]

oneToTen = list(range(10))

randlist = randlist + oneToTen

print(randlist[0])

print("List length: ", len(randlist))

first3 = randlist[0:3]

for i in first3:
    print("{} : {} ".format(first3.index(i),i))

print(first3[0] * 3)

print("string" in first3)

print("Index of string : ", first3.index("string"))

print("How many strings : ", first3.count("string"))

first3[0] = "New String"
print("{} : {} ".format(first3.index(i), i))

first3.append("Another")

for i in first3:
    print("{} : {}".format(first3.index(i),i))

#Problem
#Create a random list of random values 1-9

num_list = []

for i in range (5):
    num_list.append(random.randint(1,10))

for i in num_list:
    print(i)

#**Bubble Sort**#
#1.An outer loop decreases in size each time
#2.The goal is to have the largest number at the end of the list when the outer loop completes 1 cycle
#3.The inner loop startes comparing indexes at the beginning of the loop
#4. Check if list[Index] > list[Index + 1]
#5.If so swap the index values
#6.When the inner loop completes the largest number is at the end of the list
#7. Decrement the outer loop by 1
while i > 1:
    j = 0

    while j < i:

        if num_list[j] > num_list[j +1]:

            temp = num_list[j]
            num_list[j] = num_list[j +1]
            num_list[j +1 ] = temp
        else:
            print()

        j += 1
    i -= 1
for k in num_list:
    print(k, end=" , ")
print()


num_list = []

for i in range (5):
    num_list.append(random.randint(1,10))

for i in num_list:
    i = len(num_list) - 1

while i > 1:

    j = 0

    while j < i:

        print("\n Is {} > {}".format(num_list[j], num_list[j+1]))
        if num_list[j] > num_list[j + 1]:

            print("Switch")

            temp = num_list[j]
            num_list[j] = num_list[j + 1]
            num_list[j + 1] = temp
        else:
            print("Dont Switch")

        j += 1
        for k in num_list:
            print(k,end=", ")
        print()

    print("End of Round")

    i -= 1
for k in num_list:
    print(k,end=",")

print()

#More List functions (Sort, Reverse, Insert, Remove, Pop)

num_List = []
for i in range (5):
    num_List.append(random.randrange(1,10))

num_List.sort()

num_List.reverse()

#Inserting using indexs
num_List.insert(5,10)

num_List.remove(10)

num_List.pop(2)

for k in num_List:
    print(k, end= " ,")
print()

#List comprehasion - preform an action on each item in the list

#Static list
evenList = [i * 2 for i in range(10)]

for i in evenList:
    print(i)

numList=[1,2,3,4,5]

listOfValues = [[math.pow(m, 2), math.pow(m,3), math.pow(m, 4)]
                for m in numList]

for i in listOfValues:
    print(i)
print()
#Multi Dimenonal List
multiDlist = [[0] * 10 for i in range(10)]

multiDlist[0][1] =10

print(multiDlist[0][1])


listTable = [[0] * 4 for i in range(4)]

#Changes the first value
for i in range(4):
    #To change second value
    for j in range(4):
        listTable[i][j] = "{}   {}".format(i, j)

for i in range(4):
    for j in range(4):
        print(listTable[i][j], end = "  ")
    print()
'''

#Multiplication Table: Problem

#Create the multidimensional list
mutlTable = [[0] * 10 for i in range(10)]

# Increment with outer for
for i in range(1, 10):
    # Increment with inner for loop
    for j in range(1, 10):
        # Assign the value to the cell
        mutlTable[i][j] = i * j
# Output the data
for i in range (1, 10):
    for j in range (1, 10):
        print(mutlTable[i][j], end = " , ")
    print()