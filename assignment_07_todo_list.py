# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def addTask(todolist):
    task = input("Enter task:")
    todolist.append(task)
    print(f"Task added: '{task}'")
    return
    
def deleteTask(todolist):
    task_no = input("Enter task number to delete: ")
    if not task_no.isdigit() or int(task_no) <= 0 or int(task_no) > len(todolist):
        print("Error: Invalid input")
        return
        
    print(f"Task '{todolist[(int(task_no) - 1)]}' has been removed.")
    del todolist[int(task_no) - 1]
    
    return
    
def viewTasks(todolist):
    if len(todolist)==0:
        print("There are no tasks in your to-do list.")
        return
    result = "Your Tasks:\n"
    
    for i in range(1,len(todolist)+1):
        result += f"{i}. {todolist[i-1]}\n"
    print(result)
    return
    
def quit():
    print("Goodbye!")
    return
    
print(f"""============================
      TO-DO LIST MENU
============================
   1. Add task
   2. View tasks
   3. Delete task
   4. Quit
""")
   

todolist = []
while True:
    choice = input("\nEnter your choice (1-4): ")
    if choice =='1':
        addTask(todolist)
    elif choice == '2':
        viewTasks(todolist)
    elif choice =='3':
        deleteTask(todolist)
    elif choice == '4':
        quit()
        break
    else:
        print("Error: Invalid input")