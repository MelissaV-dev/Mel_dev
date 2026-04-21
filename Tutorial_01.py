#Name: Melissa Vaziri
#Student Number: #101366349
#Date: 09/18/2025
#Teacher: Robert Collier

#This Is Inputting The Phone Into The Print Statement
phone = input("Enter your seven-digit phone number?")

#The Prefix And Modulo Are Being Converted From A Variable To An Integer
#The //10000 For Prefix Means That It Will Give Me All The Numbers, but not the last 4 numbers
#The % For The Modulo Means That It Will Give Me The Last 5 Numbers
prefix = int(phone)//10000
modulo = int(phone)%100000

#This Statement Is Basically Assigning Answer1 As A Variable Location For The Term Prefix, Then Increasing It By 500
answer1 = prefix * 500

#This Print Is Stating That The Use Of An F-String Is Being Put Into Place, In Which An Expression Like Answer1 Is Being Placed Into The Curly Brackets
print(f"your prefix is {prefix}. Multiply this by 500, and the result is:{answer1} ")

#This Statement Is Basically Saying That Answer2 Is Answer1 + 10 * 60 Which Is What You Will Receive As A Total For Answer2
answer2 = (answer1 + 10) * 60

#This Print Is Stating That The Use Of An F-String Is Being Put Into Place, In Which An Expression Like Answer2 Is Being Placed Into The Curly Brackets
print(f" Add 10 to that result and multiply this by 500, and the result is:{answer2}")

#This Line Calculates Answer3 By Adding Answer2, And The Modulo As They Multiply It 3 Times
answer3 = answer2 + modulo * 3

#This Print Is Stating That The Use Of An F-String Is Being Put Into Place In Which An Expression Like Answer3 Is Being Placed Into The Curly Brackets
print(f" Your line number is {modulo}. Add this to the previous result three times, and the result is: {answer3}")

#This Statement Is Indicating That In Order To Get Answer4 You Need To Do Answer3 - 600 // 3
answer4 = (answer3 - 600) // 3

#This Print Is Stating That The Use Of An F-String Is Being Put Into Place, In Which An Expression Like Answer4 Is Being Placed Into The Curly Brackets
print(f"Subtract 600 from that result and divide it by 3, and the result is: {answer4}")