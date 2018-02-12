'''
#Dictionaries and Recurive Functions

#Dictonaries (Key value pairs) and non seqenual

personDict = {"fname" : "Derek" , "lname" : "Banas",
              "address" : "123 Main St"}

print("May Name :", personDict["fname"])

#make changes to already exisiting values
personDict["address"] = "215 North St"

# inserting a new key as "city"
personDict["city"] = "Pittsburgh"

#Check if there is a value for city
print("Is there a city: " , "city" in personDict)

#Printing out the values
print(personDict.values())
#Printing out the keys
print(personDict.keys())

#For loop to print both

for k, v in personDict.items():
    print(k, v)

#Searches for
print(personDict.get("mName" , "Not here"))

#Deleting Key
del personDict["fname"]

for i in personDict:
    print(i)

#Clears the entire dictionary
personDict.clear()

employees = []

fName, lName, = input("Enter employee name:" ).split()

employees.append({"fName " : fName, "lName" : lName })

print(employees)

#Problem: Create a UI where customers are asked to

#Create an array
customers = []

while True:

    # Cut off the 1st letter to cover if the user
    # types a n or y
    createEntry = input("Enter Customer (Yes/No) : ")
    createEntry = createEntry[0].lower()

    if createEntry == "n":

        # Leave the while loop when n is entered
        break
    else:

        # Get the customer name by splitting at the space
        fName, lName = input("Enter Customer Name : ").split()

        # Add the dictionary to the array
        customers.append({'fName': fName, 'lName': lName})

# Print out customer list
for cust in customers:
    print(cust['fName'], cust['lName'])


# ---------- RECURSIVE FUNCTIONS ----------
# A function that refers to itself is a recursive function

# Calculating factorials is commonly done with a recursive
# function 3! = 3 * 2 * 1

def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num-1)
        return  result
print("4! = " , factorial(4))

# 1st : result = 4 * factorial(3) = 4 * 6 = 24
# 2nd : result = 3 * factorial(2) = 3 * 2 = 6
# 3rd : result = 2 * factorial(1) = 2 * 1 = 2

# ---------- PROBLEM : CALCULATE FIBONACCI NUMBERS ----------
# To calculate Fibonacci numbers we sum the 2 previous
# values to calculate the next item in the list like this
# 1, 1, 2, 3, 5, 8 ...

# The Fibonacci sequence is defined by:
# Fn = Fn-1 + Fn-2
# Where F0 = 0 and F1 = 1

#Sample Run: print(fib(3))

#1st : result = fib(2) <-(fn-1) + fib(1) <-(fn-2) : 2 + 1

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result  = fib(num-1) + fib(num-2)
        return result

print(fib(8))
print(fib(12))
'''