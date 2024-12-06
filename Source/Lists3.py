'''
Script: Lists3.py
By: Jorge Dionisio
Purpose: Nested Lists

Revision History:
Alpha Version: 06DEC24

Notes: Please read the script as it has comments on the code
'''
__author__ = "Jorge Dionisio <L00177788@atu.ie>"
__date__ = "06 December 2024"
__version__ = "06DEC24"
__credits__ = "My wonderful wife for all the patience she has to put up with me"

my_list_1 = [1,2,3,4,"A"]
my_list_2 = ["S","T","Fish",9,10]
concatenated_list = [my_list_1, my_list_2]
print(concatenated_list)
# assign the second list within a list to a variable
second_list_in_list = concatenated_list[1]
print(second_list_in_list)
# assign the third element of the second list within a list of lists to a variable
third_element_in_second_list = concatenated_list[1][2]
print(third_element_in_second_list)