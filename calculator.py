"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True: 
    input_string = input()
    tokens = input_string.split(" ")
    operator = tokens[0]
    operators = ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']
    

    if len(tokens) <= 1:
        print("Not enough arguments, please enter at least 2.")

    elif len(tokens) <= 2:
        if tokens[1].isdigit():
            num1 = float(tokens[1])
            num2 = 0
        else:
            print("Please enter a valid number.")
       
    elif len(tokens) > 3: 
        print("Too many arguments, please enter only up to 3.")

    else:
        num1 = float(tokens[1])
        num2 = float(tokens[2])

    if input_string == 'q':
        break

    elif operator in operators:
        if operator == '+':
            print(add(num1, num2))
    else:
        print('Not a valid operator.')    


# Your code goes here
