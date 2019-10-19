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
        print("Not enough arguments, please enter at least 2")

    elif len(tokens) <= 2:
        num1 = float(tokens[1])
        num2 = 0
        print(num2)

    else:
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        print(num2)

    if input_string == 'q':
        break

    elif tokens[0] in operators:
        if tokens[0] == '+':
            print(float(add(int(tokens[1]), int(tokens[2]))))
    else:
        print('Not a valid operator.')    


# Your code goes here
