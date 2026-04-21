#Name: Melissa Vaziri
#Student Number: #101366469
#Date: 09/23/2025
#Teacher: Robert Collier


#Defining The Main Function In Which My Code Will Commence
def main():
    #Asking The User For The Average Grade Received For Each Course Component
    grade_tutorials = float(input("Enter the tutorials grade from (0-100): "))
    grade_quizzes = float(input("Enter the quizzes grade from (0-100): "))
    grade_assignments = float(input("Enter the assignments grade from (0-100): "))
    grade_final_exam = float(input("Enter the final exam grade from (0-100): "))

    #Course Outline Assessment Scheme Weight + Final Grade Calculated By The Weighted Average Of Each Task
    final_numeric_grade = (
        grade_assignments * 0.4 +
        grade_tutorials * 0.1 +
        grade_quizzes * 0.3 +
        grade_final_exam * 0.2
    )

    #This Is Basically An F-string That Allows You To Insert A Variable Into Curly Brackets Like [Final_Numeric_Grade]
    #.2f Basically Specifies A Number In Which It Is Being Rounded To Two Decimal Places
    print(f"This is the final weighted average: {final_numeric_grade:.2f}")

    #Determine The Letter Grade
    #Else If Statements Are Basically There To Check Other Conditions After The If Condition
    #If The Final_Numeric_Grade Is Greater Than or Equal To 90, The Grade Will Be An "A+" (For Example)

    if final_numeric_grade >= 90:
        grade = "A+"
    elif final_numeric_grade >= 85:
        grade = "A"
    elif final_numeric_grade >= 80:
        grade = "A-"
    elif final_numeric_grade >= 77:
        grade = "B+"
    elif final_numeric_grade >= 73:
        grade = "B"
    elif final_numeric_grade >= 70:
        grade = "B-"
    elif final_numeric_grade >= 67:
        grade = "C+"
    elif final_numeric_grade >= 63:
        grade = "C"
    elif final_numeric_grade >= 60:
        grade = "C-"
    elif final_numeric_grade >= 57:
        grade = "D+"
    elif final_numeric_grade >= 53:
        grade = "D"
    elif final_numeric_grade >= 50:
        grade = "D-"
    else:
        grade = "F"
 #This Is Also An F-String In Which It allows You To Insert A Variable Into A Curly Bracket, Such As {Grade}
    print(f"Your letter grade is: {grade}")

#Call The Function
main()