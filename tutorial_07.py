#Name : Melissa Vaziri
#Student Number : # 101366349
#Partner's Name: Adrian Long
#Partner's Student Number: # 101376444

# ======== TABLE OF CONTENTS ======== #
# Stage 0 - Initially ************** 18
# Stage 1 - Foundation ************* 26
# Stage 2 - Degrees/Radians ******** 87
# Stage 3 - Taylor Series ********* 184
# Stage 4 - Iterative Factorial *** 265
# Stage 5 - Review/Testing ******** 347





# ====== Stage 0 ====== #
# Navigator: Melissa
# Driver: Adrian





# ====== Stage 1 ====== #
# Navigator: Melissa
# To convert degrees into radians, you need to use the formula that states that radians = degrees x (pi/180)
# We can use a float literal to represent decimal numbers, such as pi = 3.141592653589793
#Steps:
#1. Take the measure of the angles in degrees
#2. Multiply the conversion factor, which is pi by 180
#3. The result will provide the angle measured in radians

# Driver: Adrian
# def sin(x: float) -> float:
#     pass
# def cos(x: float) -> float:
#     pass
#
# def taylor_series():
#     pass
# def factorial(x:int) -> int:
#     pass
#
# def to_radians(degrees: float) -> float:
#     pass
# def to_degrees(radians: float) -> float:
#     pass
#
# def main():
#     # declare a list of operations
#     operations = ["sin","cos"]
#
#     # loop until the user exits
#     while True:
#
#         # get the user input
#         calculation = input("Calculator:\n"
#                             "1. Calculate sin(x)\n"
#                             "2. Calculate cos(x)\n"
#                             "Enter '1', '2' or 'quit': ")
#
#         # quit if the user entered quit
#         if calculation.lower() == "quit":
#             break
#
#         # prompt for the user would like to use for their calculation
#         value = float(input("What is the value of x for your calculation in degrees? "))
#
#         # calculate the result of the operation the user selected
#         result = None
#         if calculation == "1":
#             calculation = 0
#             result = sin(value)
#         else:
#             calculation = 1
#             result = cos(value)
#
#         # print sin(value) == result or cos(value) == result depending on what the user selected
#         print(f"{operations[calculation]}({value:.4f}) == {result:.4f}")
# main()




# ====== Stage 2 ====== #
# Navigator: Adrian
# The idea of a taylor series is to a proximate a given function as accurately as possible by changing the coefficients
# of a polynomial.
# To approximate cos it first makes sense that at x = 0, our function should also be 1.

# cos(0) = 1
# f(x) a + bx + cx^2
# cos(0) = f(0)
# 1 = 1 + 0*x + 0*x^2

# f(x) = 1 + ax + bx^2
# secondly it also makes sense that the tangent line at x = 0 for f(x) should be the same as for cos.
# d cos(x) / dx (0) = -sin(0) = 0
# therefore f`(x) should also equal zero 0
# d f / d x = b + 2x
# d f / d x (0) = b + 2(0) so b should be zero

# f(x) = 1 + 0x + cx^2
# thirdly
# the third derivative os cos(x) is -1
# f``(0) = -1
#     -1 = 2c
#      c = -1/2

# f(x) = 1 + 0x + (-1/2)*x^2

# the overall pattern is the following:
# f(x) = 1 + 0*[(x^1)/(1!)] + -1[(x^2)/(2!)] + 0[(x^3)/(3!)] + 1[(x^4)/(4!)] + ...
# result = 1
# result += ((i % 2) * -1) * [(x^(2i - 1))/((2i-1)!)]
# this stuff is complicated

# Driver: Melissa
# PI = 3.141592653589793  # This Is The Value Of Pi
#
# def sin(x: float) -> float:
#     pass
# def cos(x: float) -> float:
#     pass
#
# def taylor_series():
#     pass
# def factorial(x:int) -> int:
#     pass
#This function converts radians to degrees
# def to_radians(degrees: float) -> float:
#     #Using the Formula to find the radians
#     radians = degrees * (PI / 180)
#     #This will return the radians output
#     return radians
#
#This function converts degrees to radians
# def to_degrees(radians: float) -> float:
#     #Using the provided formula, will convert from degrees to radians
#     degrees = radians * (180 / PI)
#     #Lastly, return the degrees
#     return degrees
#
# def main():
#     # declare a list of operations
#     operations = ["sin","cos"]
#
#     # loop until the user exits
#     while True:
#
#         # get the user input
#         calculation = input("Calculator:\n"
#                             "1. Calculate sin(x)\n"
#                             "2. Calculate cos(x)\n"
#                             "Enter '1', '2' or 'quit': ")
#
#         # quit if the user entered quit
#         if calculation.lower() == "quit":
#             break
#
#         # prompt for the user would like to use for their calculation
#         value = float(input("What is the value of x for your calculation in degrees? "))
#
#         # calculate the result of the operation the user selected
#         result = None
#         if calculation == "1":
#             calculation = 0
#             result = sin(value)
#         else:
#             calculation = 1
#             result = cos(value)
#
#         # print sin(value) == result or cos(value) == result depending on what the user selected
#         print(f"{operations[calculation]}({value:.4f}) == {result:.4f}")
#
# main()





# ====== Stage 3 ====== #
# Navigator: Melissa
# Driver: Adrian
# import math
#
# PI = 3.141592653589793  # This Is The Value Of Pi
#
# def sin(radians: float) -> float:
#     return cos(radians + PI / 2) # sin is just cos but offset by pi/2
#
# def cos(radians: float) -> float:
#     return taylor_series(radians, 15)
#
# def factorial(x: int) -> int:
#     return math.factorial(x)
#
# def taylor_series(radians:float, accuracy:int) -> float:
#     result = 1
#     for i in range(1,accuracy):
#         exponent = 2 * i
#         sign = (-1) ** i
#         result += sign * ((radians ** exponent) / (factorial(exponent)))
#     return result
#
# # This function converts radians to degrees
# def to_radians(degrees: float) -> float:
#     # Using the Formula to find the radians
#     radians = degrees * (PI / 180)
#     # This will return the radians output
#     return radians
#
#
# # This function converts degrees to radians
# def to_degrees(radians: float) -> float:
#     # Using the provided formula, will convert from degrees to radians
#     degrees = radians * (180 / PI)
#     # Lastly, return the degrees
#     return degrees
#
#
# def main():
#     # declare a list of operations
#     operations = ["sin", "cos"]
#
#     # loop until the user exits
#     while True:
#
#         # get the user input
#         calculation = input("Calculator:\n"
#                             "1. Calculate sin(x)\n"
#                             "2. Calculate cos(x)\n"
#                             "Enter '1', '2' or 'quit': ")
#
#         # quit if the user entered quit
#         if calculation.lower() == "quit":
#             break
#
#         # prompt for the user would like to use for their calculation
#         value = float(input("What is the value of x for your calculation in degrees? "))
#
#         # convert degrees to radians
#         value %= 180
#         value = to_radians(value)
#
#         # calculate the result of the operation the user selected
#         result = None
#         if calculation == "1":
#             calculation = 0
#             result = sin(value)
#         else:
#             calculation = 1
#             result = cos(value)
#
#         # print sin(value) == result or cos(value) == result depending on what the user selected
#         print(f"{operations[calculation]}({value:.4f}) == {result:.4f}")
#
# main()




# ====== Stage 4 ====== #
# Navigator: Adrian
# !10 = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
# basically iterate up to 10, multiplying the result each time

# Driver: Melissa
PI = 3.141592653589793  # This Is The Value Of Pi

def sin(radians: float) -> float:
    return cos(radians - PI / 2) # sin is just cos but offset by pi/2

def cos(radians: float) -> float:
    return taylor_series(radians, 10)

def factorial(x: int) -> int:
    result = 1
    for i in range(1,x + 1):
        result *= i
    return result

# calculate the taylor series for cos
def taylor_series(radians:float, accuracy:int) -> float:
    radians %= 2 * PI
    result = 1
    for i in range(1,accuracy):
        # perform utter witchcraft
        exponent = 2 * i # <- the exponent for this iteration
        sign = (-1) ** i # <- the + or - sign for addition or subtraction
        result += sign * ((radians ** exponent) / (factorial(exponent))) # <- Calculate the i th iteration of the taylor series

    return result

# This function converts radians to degrees
def to_radians(degrees: float) -> float:
    # Using the Formula to find the radians
    radians = degrees * (PI / 180)
    # This will return the radians output
    return radians

# This function converts degrees to radians
def to_degrees(radians: float) -> float:
    # Using the provided formula, will convert from degrees to radians
    degrees = radians * (180 / PI)
    # Lastly, return the degrees
    return degrees

def main():
    # declare a list of operations
    operations = ["sin", "cos"]

    # loop until the user exits
    while True:

        # get the user input
        calculation = input("Calculator:\n"
                            "1. Calculate sin(x)\n"
                            "2. Calculate cos(x)\n"
                            "Enter '1', '2' or 'quit': ")

        # quit if the user entered quit
        if calculation.lower() == "quit":
            break

        # prompt for the user would like to use for their calculation
        value = float(input("What is the value of x for your calculation in degrees? "))

        # convert degrees to radians
        value = to_radians(value)

        # calculate the result of the operation the user selected
        result = None
        if calculation == "1":
            calculation = 0
            result = sin(value)
        else:
            calculation = 1
            result = cos(value)

        # print sin(value) == result or cos(value) == result depending on what the user selected
        print(f"{operations[calculation]}({value:.4f}) == {result:.4f}")


# ====== Stage 5 ====== #
#Navigator: Melissa
#First Test: cos (4) in degrees gave me the correct response of 0.9976
#Second Test: The value of x for my calculation in degrees for 5 is sin (5) = 0.0872
#Third Test: the value of x for my calculation in degrees for 67 is cos (67) with the correct response of 0.3907
#Fourth Test: the value of x for my calculation in degrees 8 is cos (8) with the correct response of 0.9903
#Fifth Test: the value of x for my calculation in degrees 9 is sin (9) with the correct response of 0.1564

# Driver: Adrian
# To Test that our code worked I wanted to compare our implementation against the one in math from python.
# To do this I used a brute force approach where I tested several values in the range [0,360) for both sin and cos
# I then calculate the percent error and percent difference then print a line of numbers in CSV format.
# Running this code I saw that our code performs decently well for only doing 11 iterations of the taylor series

# Some known issues are:
    # - Our input method sometimes will cause a value exception when casting the users input to a float.
        # IE: If they did not enter a float

# Our factorial function elegantly handles value less than -1 because the loop simply wouldn't process,
# therefore our original value of 1 is unmodified and returned
import math

def to_four_decimals(x: float) -> float:
    return int(x * (10 ** 5)) / (10 ** 5)
def percent_error(experimental_value: float, accepted_value: float) -> float:
    if accepted_value == 0:
        return abs(experimental_value - accepted_value)
    return (experimental_value - accepted_value) / accepted_value * 100
def percent_difference(value1:float, value2:float) -> float | None:
    if value1 + value2 == 0:
        return None
    return abs(value1 - value2) / ((value1 + value2) / 2)

def tests():
    print("function, expected, actual, percent_error, percent_difference,")
    for x in range(360):
        expected = math.sin(math.radians(x))
        actual   = sin(to_radians(x))
        print(f"sin({x}), {expected:.4f}, {actual:.4f}, {percent_error(actual,expected)}, {percent_difference(actual,expected)}, ")

    for x in range(360):
        expected = math.cos(math.radians(x))
        actual   = cos(to_radians(x))
        print(f"cos({x}), {expected:.4f}, {actual:.4f}, {percent_error(actual,expected)}, {percent_difference(actual,expected)}, ")

tests()
main()
