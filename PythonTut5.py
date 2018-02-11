#Functions
'''
def add_numbers(num1, num2):
    return num1 + num2
print("5 + 4 = ", add_numbers(5,4))


#local variables cant be used
def assign_name():
    name = "Doug"
assign_name()
print(name)
#Error:Name not defined

def change_name(name):
    name = "Mark"

name = "Tom"

change_name(name)
print(name)
# Will print Tom

#Adding Return will overide the local name
def change_name(name):
    return  "Mark"

name = "Tom"

change_name(name)
print(name)

gbl_name = "Sally"

def change_name():
    global gbl_name
    gbl_name = "Sammy"


change_name(name)
print(gbl_name)

# -> will change the global to Sammy

def get_sum(num1, num2):
    sum = num1 + num2

print(get_sum(5, 4))
# -> Will return "NONE


#Problem : Solve for x
# x + 4 = 9

# x will always be the 1st value received and you only
# will deal with addition

def solve_x(equation):

#Recieve the string and split the string into variables
    x, operator, num1, equal, num2 = equation.split()


    #Convert the strings into ints
    num1, num2 = int(num1), int(num2)
    #Conver the results into a string and join it to the string "X = "
    #return "x = " + str(num2 - num1)
    return "x = " + str(num2 / num1)

#print outside of function
#print(solve_x("x + 4 = 9"))
print(solve_x("x * 5 = 20"))


#Return Multiple Values

def  mult_divide(num1, num2):
    return (num1 * num2), (num1 / num2)
mult, divide = mult_divide(5,4)

print ("5 * 4 =", mult)
print ("5 / 4 =", divide)


# A prime can only be divided by 1 and itself
# 5 is a prime 1 and 5 = positive factor
# 6 is not prime 1, 2, 3, 6

#Input max prime
# Use a for loop and check if % == 0 True(returns remainder)

def is_prime(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

def get_Primes(max_number):

    list_of_primes = []

    for num1 in range(2, max_number):
        if is_prime(num1):
            list_of_primes.append(num1)
    return list_of_primes
max_num_to_check = int(input("Search for Primes up to :"))

list_of_primes = get_Primes(max_num_to_check)

for prime in list_of_primes:
    print(prime)

#Using *args

def sumAll(*args):
    sum = 0

    for i in args:
        sum += i

    return sum
print("Sum", sumAll(1,2,3,4,5))


import math

def get_area(shape):
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    elif shape == "parallelogram":
        parallelogram_area()
    elif shape == "rhombuse":
        rhombuses_area()
    elif shape == "triangle":
        triangle_area()
    elif shape == "trapezoids":
        trapezoid_area()
    else:
        print("Please enter rectangle or circle")

def parallelogram_area():
    base = float(input("Enter base:"))
    height = float(input("Enter height"))

    area = base * height

    print("The area of the parallelogram is" ,area)

def rhombuses_area():
    base_1 = float(input("Enter Base 1"))
    base_2 = float(input("Enter Base 2"))

    area = ((base_1 * base_2) / 2)

    print("The area of the rhombus is" , area)


def triangle_area():
    base = float(input("Enter the base"))
    height = float(input("Enter the height"))

    area = ((height * base) / 2 )

    print("The area of the triangle is" , area)

def trapezoid_area():
    base_1 = float(input("Enter the first base"))
    base_2 = float(input("Enter the second base"))
    height = float(input("Enter the height"))

    area = ((((base_1 + base_2) / 2)) * height)
    print ("The are of the trapezoid is :", area)



def rectangle_area():
    length = float(input("Enter the length"))
    width = float(input("Enter the width"))

    area = length * width

    print("The area of the rectangle is", area)

def circle_area():
    radius = float(input('Enter the radius: '))

    area = math.pi * (math.pow(radius,2))

    print ("The area of the circle is:{:.2f}".format(area))

def main():

    shape_type = raw_input("Get Area for what shape :")

    get_area(shape_type)


main()

'''