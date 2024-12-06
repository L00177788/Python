'''
Script: Lists3.py
By: Jorge Dionisio
Purpose: Examples of methods of lists

Revision History:
Alpha Version: 06DEC24

Notes: Please read the script as it has comments on the code
'''
__author__ = "Jorge Dionisio <L00177788@atu.ie>"
__date__ = "06 December 2024"
__version__ = "06DEC24"
__credits__ = "My wonderful wife for all the patience she has to put up with me"

my_list = ["One", "Two", "Three"]
print(my_list)
my_list.append("Four")
# Appended another element
my_list.append("Five")
print(my_list)

my_string = "12/9/22, 14:30, System Start, UB2204-Server, MyServer"
list_of_values = my_string.split(",")
# You can append as well here
list_of_values.append("Append example")
print(list_of_values)

my_list_2 = ["Four", 5, "Six"]
# Extended the list with my_list_2
my_list.extend(my_list_2)
print(my_list)

# Example of insertion of an element in the first position
my_list.insert(0, "First")
print(my_list)

# Example of removing an element
my_list.remove("Four")
print(my_list)

# Example of trying to remove an element that does not exist
try:
    my_list.remove("I don't exist")
except ValueError:
    print("Element does not exist in the list")

# Example of pop, in this case since no argument was specified it returns and removes the last element of the list
last_element = my_list.pop()
print(last_element)

# Example of index, to search a list for a value
index_of_two = my_list.index("Two")
print(index_of_two)

# Example of count, to count how many times a value appears in the list
count_list = [1,1,1,3,3,3,3,3,4,4]
how_many_times_three = count_list.count(3)
print(how_many_times_three)

# Example of sort, sorts a list
list_to_sort = ["D", "C", "A"]
list_to_sort.sort()
print(list_to_sort)

# Example of reverse, reverses the elements in place
list_to_sort.reverse()
print(list_to_sort)

# Example of clear, clears the list
list_to_sort.clear()
print(list_to_sort)

# Example of copy, creates a shallow copy of the list
second_list = my_list.copy()
print(second_list)
