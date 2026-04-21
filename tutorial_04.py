# Name: Melissa Vaziri
# Student Number: 101366349

import random

def main():
    #Assign N As An Integer Input Representing The List Size
    n = int(input("How long would you like the initial list to be? "))

    #Implementing An Empty List To Store Random Integers
    my_list = []

    # Initializing A Loop That Repeats Over And Over Again
    for i in range(n):

        # Append Is Basically Added At The End Of My List (Like For A Numerical Value) Into A Random Integer From 1 To 20
        my_list.append(random.randint(1, 20))

    # This Is Printing My Statement
    print("The initial list:", my_list)

    # Initiating An Event-Controlled Loop For Replacing a Number
    # If This Statement Is True, It Will Take The Replacing number, And Ask The User What They Would Like To Replace It With As A String
    # If The User Picks -1 As The Replacement Number, Then They Will Exit, But Also Print A Goodbye Statement
    while True:
        number = int(input("What number would you like to replace (or -1 to exit)? "))
        if number == -1:
            break  # Exit The Loop If User Enters -1

        replacement = input("What string would you like to use as a replacement? ")

        # This Will Be Replacing All The Equivalent Numbers With A String
        # If N Is In The Range My List, Then N Will Be Equivalent To The Replacement Number, And The Replacement String
        # Len Is How Long Is The Line Of The Numbers Of The List

        for i in range(len(my_list)):
            if my_list[i] == number:
                my_list[i] = replacement

        # This Is Printing My Statement
        print("New List:", my_list)

    print("Goodbye!")

# Run the main function
main()