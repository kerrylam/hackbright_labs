"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True: 
    input_string = input()
    tokens = input_string.split(" ")
    
    if input_string == 'q':
        break

# Your code goes here
