# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def addStudent(studentList):
    name = input("Student name: ")
    st_id = input("Student ID: ")
    if not st_id.isdigit() or int(st_id)<=0:
        print("Error: Invalid input")
        return
    score_no = input("How many scores? ")
    scores = []
    if not score_no.isdigit() or int(score_no) <=0:
        print("Error: Invalid input")
        return

    for i in range(1, int(score_no) + 1):
        score = input(f"Enter score {i}: ")
        if not score.isdigit() or int(score) < 0 or int(score) > 100:
            print("Error: Invalid input")
            return
        scores.append(int(score))
       
    student = {
        "name":name,
        "id":st_id,
        "scores":scores
    }
    studentList.append(student)
    print(f"Student '{name}' has been successfully added.")
    return

    
def average_score(studentList):
    if len(studentList)==0:
        print("No student has been added yet.")
        return
    st_id = input("Enter student ID: ")
    if not st_id.isdigit() or int(st_id)<=0:
        print("Error: Invalid input")
        return
    total = 0
    score_no = 0
    for student in studentList:
        for key, value in student.items():
            if st_id==value:
                result = f"{student['name']}'s average score: "
                total = 0
                score_no = len(student["scores"])
                for i in student["scores"]:
                    total += i
    if score_no==0:
        print("There is no student with that ID.")
        return        
    average = total/score_no
    result+= f"{round(average,2)}"
    print(result)
    return
    
    
def display_table(studentList):
    if len(studentList) == 0:
        print("No student has been added yet.")
        return
    print('='*50)
    print("Student Name\tStudent ID\tScores\tAverage Score")
    print('='*50)
    for student in studentList:
        total= 0
        score_no = len(student["scores"])
        for i in student["scores"]:
            total += i
        scores = [str(x) for x in student["scores"]]
        print(f"{student['name']}\t{student['id']}\t{','.join(scores)}\t{round(total/score_no,2)}")
    return
    
def quit():
    print("Goodbye!")
    return
    
print(f"""================================
   STUDENT RECORD SYSTEM MENU
================================
   1. Add student
   2. Display all students
   3. Calculate average score
   4. Quit
   """)
   
studentList = []
while True:
    choice = input("\nEnter your choice (1-4): ")
    if choice =='1':
        addStudent(studentList)
    elif choice == '2':
        display_table(studentList)
    elif choice =='3':
        average_score(studentList)
    elif choice == '4':
        quit()
        break
    else:
        print("Error: Invalid input")