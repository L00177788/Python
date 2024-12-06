'''
Script: Lists2.py
By: Jorge Dionisio
Purpose: List contacenation examples

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
# Added this list with only strings inside
my_list_3 = ["Jorge", "Guida"]
# Concatenation of three lists
concatenated_list = my_list_1 + my_list_2 + my_list_3
# Printing the concatenated list
print(concatenated_list)
my_list_4 = [4, "Jorge"]
# if we don't need to keep ordering we can do subtraction with sets
subtraction_list = list(set(concatenated_list) - set(my_list_4))
print(subtraction_list)
# If we need to keep ordering, here's an example
class MyList(list):
    """This is my implementation that supports subtraction of lists"""
    def __init__(self, *args):
        """Implementation of the constructor with a super of list"""
        super(MyList, self).__init__(args)

    def __sub__(self, otherlist):
        """Override of the - operator"""
        return self.__class__(*[item for item in self if item not in otherlist])
# Now that we have the new class defined, we can use it
my_list_5 = MyList(1,2,3,4,"A","Jorge")
my_list_6 = MyList(4,"Jorge")
subtraction_list = my_list_5 - my_list_6
print(subtraction_list)