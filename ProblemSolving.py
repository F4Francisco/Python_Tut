#Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures

user_input = input("Enter the string")

while True:
    for i in range(0, len(user_input)):
        print(user_input[i])

    for i in reversed(user_input):
        print(i)
    if (user_input != i):
        print("True")



