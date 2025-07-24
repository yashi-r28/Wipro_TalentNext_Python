'''
Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go and meet him.
He challenges you to find it out without seeing the content of the file. He has given hints to find it. Let's surprise him by breaking the challenge with our python code.
'''

import re
from collections import Counter

def get_meeting_details(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
       
        num_lines = len(lines)
        if num_lines == 0:
            return "File is empty."
        
        if num_lines <= 12:
            meeting_time = f"{num_lines} AM"
        else:
            hour = num_lines % 12
            hour = 12 if hour == 0 else hour
            meeting_time = f"{hour} PM"
        
        text = ' '.join(lines).lower()
        words = re.findall(r'\b\w+\b', text)
        word_freq = Counter(words)
        
   
        most_common_word, _ = word_freq.most_common(1)[0]
        
        print(f"Meeting time: {meeting_time}")
        print(f"Meeting place: {most_common_word.capitalize()} Street")
    
    except FileNotFoundError:
        print("File not found. Please check the file name and path.")

get_meeting_details("sample.txt")
