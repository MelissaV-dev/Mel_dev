# Name: Melissa Vaziri
# Student Number: 101366349

# Function To Check If A Number Is Prime
# Type Hinting Specifies The Types Of Arguments A Function Allows, And The Type Of Returning Value

def prime (n:int) -> bool:


    #Numbers Less Than Or Equal To 1 Are Not Considered Prime Numbers
    if n <= 1:

        return False

#Check For Factors For 2 To N
    for i in range(2, n):

        #If N Can Be Divided By Any Number In That Specific Range (Not Prime)
        if n % i == 0:


            return False

        # Return True If The User Enters An Integer Greater Than 1 That Was Not Divisible By Any Number Between 2 And N ( It Is Prime)
    return True

def main() -> None:

    while True:
        #Asking The User To Enter Any Int, If Not, They Can Use The Letter L To Leave
        user_input = input("Enter any integer (or 'l' to leave): ")

        #Using User_input.lower() To Indicate Uppercase Or Lowercase Letters
        if user_input.lower() == 'l':
            break

        #The Input Is Turned Into An Integer And Assigned To A Variable Number

        n = int(user_input)

       #If N Is Prime, Then It Will Print As An F String That It Is A Prime Number
       #Else It Will Say That N Is Not A Prime Number As An F String

        if prime(n):
            print(f"{n} is a prime number.")


        else:
            print(f"{n} is not a prime number.")

# Calling The Main Function

main()
