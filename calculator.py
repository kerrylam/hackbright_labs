"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True: 
    input_string = input()
    tokens = input_string.split(" ")
#    num1 = tokens[1]
#    num2 = tokens[2]
    operators = ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']

    if input_string == 'q':
        break

    elif tokens[0] in operators:
        if tokens[0] == '+':
            print(float(add(int(tokens[1]), int(tokens[2]))))
    else:
        print('Not a valid operator.')    

# Your code goes here
