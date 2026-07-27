# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
        
    return sum
    
def average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    average = (sum/len(numbers))
    
    return average
    
def maximum(numbers):
    maxVal = numbers[0]
    for number in numbers:
        if number > maxVal:
            maxVal = number
        else:
            continue
            
    return maxVal
        
def minimum(numbers):
    minVal = numbers[0]
    for number in numbers:
        if number < minVal:
            minVal = number
        else:
            continue
            
    return minVal
    

myNumbers = []
size = int(input("How many numbers? "))
for i in range(1,size + 1):
    number = int(input(f"Enter number {i}: "))
    myNumbers.append(number)

print(f"""Results:
Sum:     {sum(myNumbers)}
Average: {average(myNumbers)}
Maximum: {maximum(myNumbers)}
Minimum: {minimum(myNumbers)}""")