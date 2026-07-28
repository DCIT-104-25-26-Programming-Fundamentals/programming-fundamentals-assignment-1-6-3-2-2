# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def add(num1,num2):
    result =num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
    return
    
def subtract(num1,num2):
    result =num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
    return
    
    
def multiply(num1,num2):
    result =num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
    return
    
def divide(dividend,divisor):
    result = round(dividend / divisor, 2)
    print(f"Result: {dividend} / {divisor} = {result}")
    return
    
    
def modulus(num1,modulus):
    result = num1 % modulus
    print(f"Result: {num1} % {modulus} = {result}")
    return
    
def exponent(base,power):
    result = base ** power
    print(f"Result: {base} ** {power} = {result}")
    return
    
def quit():
    print('Goodbye!')
    return
    
    
print(f"""============================
     SIMPLE CALCULATOR
============================
   1. Addition
   2. Subtraction
   3. Multiplication
   4. Division
   5. Modulus
   6. Exponentiation
   7. Quit""")

while True:
    try:
        operation = int(input("\nSelect an operation (1-7): "))
        if not(1<=operation<=7):
            print("Error: Invalid input.")
            continue
        elif operation == 7:
            quit()
            break
            
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if str(num1).endswith('.0'):
            num1 = int(num1)
            
        if str(num2).endswith('.0'):
            num2 = int(num2)

    except ValueError:
        print("Error: Invalid input.")
        continue
        
    if operation == 1:
        add(num1,num2)
    elif operation == 2:
        subtract(num1,num2)
    elif operation == 3:
        multiply(num1,num2)
    elif operation == 4:
        if num2 == 0:
            print("Division by zero is not possible.")
            continue
        divide(num1,num2)
    elif operation == 5:
        if not(str(int(num2)).isdigit()):
            print("Error:Invalid input")
            continue
        elif num2 == 0:
            print("Division by zero is not possible.")
            continue
        modulus(num1,int(num2))
    elif operation == 6:
        exponent(num1,num2)