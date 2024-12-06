'''
Script: Lists1.py
By: Jorge Dionisio
Purpose: First Lists example in python, slicing, indexes, and printing

Revision History:
Alpha Version: 06DEC24

Notes: Please read the script as it has comments on the code
'''
__author__ = "Jorge Dionisio <L00177788@atu.ie>"
__date__ = "06 December 2024"
__version__ = "06DEC24"
__credits__ = "My wonderful wife for all the patience she has"

# Creating a list with multiple types inside it.
my_list = [1,2,3,4,"A","B",8,9]
# Getting the length of the list and assigning it to variable a
a = len(my_list)
# Printing the size of the list stored in variable a
print(a)
# Slicing the list starting in index 1, finishing in index 8 and with a step of 2 elements and storing it in variable slice_1
slice_1 = my_list[1:8:2]
# Printing slice_1 variable
print(slice_1)
# Assigning the value of the second last element of my_list to variable my_character
my_character = my_list[-2]
# Printing the variable my_charachter
print(my_character)
# Get a single element from the list
single_elem = my_list[7]
# Printing the single element
print(single_elem)