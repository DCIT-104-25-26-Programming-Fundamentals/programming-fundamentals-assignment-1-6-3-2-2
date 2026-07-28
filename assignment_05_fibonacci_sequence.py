# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def fibonacci(n):
    sequence = [0, 1]
    if n==0:
        return []
    elif n == 1:
        return [0]
    elif n < 0:
        return "Error: The number of terms cannot be negative."
    else:
        for i in range(2):
            while len(sequence) <= (n-1):
                nextVal = sequence[i-1] + sequence[i-2]
                sequence.append(nextVal)
    
    sequence = [str(i) for i in sequence]            
    result = "Fibonacci sequence: " + ' '.join(sequence)
    return result
    
n = int(input("How many terms? "))
print(fibonacci(n))


def isInFibonacci(number):
    sequence = [0, 1]
    for i in range(2):
        while sequence[-1]<= (number):
            nextVal = sequence[i-1] + sequence[i-2]
            sequence.append(nextVal)
                
    if number in sequence:
        result = f"{number} is a fibonacci number."
    else:
        result = f"{number} is NOT a fibonacci number."
        
    return result
    
number = int(input("Enter a number to check: "))
print(isInFibonacci(number))