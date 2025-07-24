'''
Write a Python function that accepts a hyphen-separated sequence of colors as input and returns the colors in a hyphen-separated sequence after sorting them alphabetically.
Constraint: All the colors will be completely in either lower case or upper case.
'''

def sort_colors(color_string):
    color_list = color_string.split('-')
    
    color_list.sort()
    
    sorted_colors = '-'.join(color_list)
    
    return sorted_colors

input1 = "green-red-yellow-black-white"
input2 = "PINK-BLUE-TAN-PURPLE"

print("Sorted colors (1):", sort_colors(input1))  # Output: black-green-red-white-yellow
print("Sorted colors (2):", sort_colors(input2))  # Output: BLUE-PINK-PURPLE-TAN


'''
Create a Python module with the following functions:
ispalindrome(name)
count_the_vowels(name)
frequency_of_letters(name)
'''
import mymodule

name = "bob"

mymodule.ispalindrome(name)
mymodule.count_the_vowels(name)
mymodule.frequency_of_letters(name)

'''

'''