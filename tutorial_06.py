import os

task_list = [] #a list to store the tasks
status_complete = "[X]" #a string that shows that the task is complete
status_not_complete = "[ ]" # a string that shows that the task is not complete

#function to add new tasks to the task list
def adding_tasks():
    #calls this function to clear the terminal before display
    clear_terminal()

    while True:
        #ask the user if they want to enter a new task
        y_n = input("Would you like to add a task to your list? (y/n)")

        if y_n.lower() == 'y':
            task = input("enter your task ")
            #append the new task to the list and marking it as not complete
            task_list.append(f"{task} {status_not_complete}")
        else:
            #if the user enters anything other than 'y'
            print("back to menu.")
            return #exit the function and return to the main loop
#--------------------------------------------------------------------------------------------------------------
#function to display the menu and returns the user input "choice_menu"
def menu():

    print("\n1. add a task. ")
    print("2. view task list. ")
    print("3. mark tast as done. ")
    print("4. exit. ")
    choice_menu = input("enter your choice(1-4): ")
    return choice_menu #return the user input
#-----------------------------------------------------------------------------------------------------------------
#function to clear the terminal
def clear_terminal():
    #checks the the operating system name to use the correct clear command
    #'posix' is common on linux/mac
    if os.name == 'posix':
        os.system('clear')
    else:
        #'cls' is the command on windows
        os.system('cls')
#----------------------------------------------------------------------------------------------------------------
#function to display the content of the task list
def display_task():
    #calls this function to clear the terminal before display
    clear_terminal()

    #checks if the list is empty
    if len(task_list) == 0:
        print("Your task list is empty! back to the menu.")
        return
    
    task_num = 1 #creates a counter to display the tasks(starts at 1 for the user; starts at 0 in the list)
    #loop through every task in the list
    for task_with_status in task_list:
        #print the task number and the task string (including its status)
        print(f"{task_num}. {task_with_status}")
        #increase the task number for the next item in the list
        task_num += 1
#------------------------------------------------------------------------------------------------------------------
#function that allows the user to mark an incomplete task as complete
def complete_task():
    #display the task list so that the user gets to pick what to mark as complete
    display_task()
    #checks if the list is empty
    if len(task_list) == 0:
        return

    while True:
        #get the number of the task the user wants to mark as complete
        task_number_string = input("enter the number of the task to mark as complete (or type 'exit' to stop): ")
        #check if the user wants to go back to the menu
        if task_number_string.lower() == "exit":
            print("going back to the menu!")
            return

        #converts the string input to an integer
        task_number = int(task_number_string)
        #the list starts at 0 not 1, this line takes the displayed number and subtracts 1 from it to match the position in the list
        task_index = task_number -1
        #it saves the content in 'task_list' at the possition 'task_index' in a new variable called 'current_task'
        current_task = task_list[task_index]

        #checks if the task is already marked as complete
        if status_complete in current_task:
            print(f"Task {task_number} is already marked as done.")
        #checks if the task is marked as incomplete in the list
        elif status_not_complete in current_task:
           #uses the '.replace()' python function to change the status of the task from incomplete to complete
           # .replace(old string, new string to replace the old one with)
           updated_task = current_task.replace(status_not_complete, status_complete)
           #update the task in the list with the new complete status
           task_list[task_index] = updated_task
           display_task()
#-----------------------------------------------------------------------------------------------------------------
#function to run the task list
def main():
    
    while True:
        #displays the menu
        choice = menu()
        
        #checks fo the user input in the function 'menu()'
        if choice == "1":
            adding_tasks() #call the function to add tasks
        elif choice == "2":
            display_task() #calls the function to view the list
        elif choice == "3":
            complete_task() #call the function to mark tasks as done
        else:
            print("exiting. goodbye!")
            break #exit the loop and ending the program

if __name__ == '__main__':
    main()