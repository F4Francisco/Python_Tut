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
'''
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