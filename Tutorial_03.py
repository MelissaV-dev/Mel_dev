# Name: Melissa Vaziri
# Student Number: 101366349
# Defining The Main Function
def main():
    while True:
        # Asking The User For An Integer
        value = input("Enter An Integer Between 1 and 9: ")

        # Checking If The Input Is A Digit and If The Value Is Between 1 And 9 Inclusive
        if value.isdigit() and 1 <= int(value) <= 9:
            # Basically, I Assigned "I" As A Variable For The Integer Of The Variable Value
            i = int(value)

            # This Is Used For A Loop That Repeats A Specific Amount Of Times
            for row in range(1, i + 1):

                # This Is Saying That Col Repeats, And Range Produces The Order of Numbers
                for col in range(row):
                    print(str(row), end="")

                # Printing Statement So That After A Number Row Is Printed, We Go To A New Line For The Next Row
                print()

            # The Break Is To Get Out Of The Loop (Finished The Triangle)
            break


# Calling The Main Function
main()