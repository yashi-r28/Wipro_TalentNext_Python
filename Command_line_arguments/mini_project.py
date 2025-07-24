'''
Through command line arguments three strings separated by space are given to you. Each string is a series of numbers separated by hyphen(-). You like all the numbers in string 1 and dislike all the numbers in string 2.
Third string contains the numbers given to you. Your initial happiness is 0.
When you encounter a number which is present in string 1, add 1 to your happiness, if it is present in string 2, add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
'''

import sys

like_str = sys.argv[1]   
dislike_str = sys.argv[2] 
given_str = sys.argv[3]  


likes = set(map(int, like_str.split('-')))
dislikes = set(map(int, dislike_str.split('-')))
given = list(map(int, given_str.split('-')))

happiness = 0

for num in given:
    if num in likes:
        happiness += 1
    elif num in dislikes:
        happiness -= 1


print(happiness)
