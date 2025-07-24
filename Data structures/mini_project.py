'''
Create a dictionary that contains a list of people and one interesting fact about each of them.

Display each person and his or her interesting fact to the screen.
Next, change a fact about one of the people.
Also add an additional person and corresponding fact.
Display the new list of people and facts.
Run the program multiple times and notice if the order changes.

'''

people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}


print("Original List:\n")
for person in people_facts:
    print(person + ":", people_facts[person])


people_facts["Jeff"] = "Is afraid of heights."


people_facts["Jill"] = "Can hula dance."


print("\nUpdated List:\n")
for person in people_facts:
    print(person + ":", people_facts[person])


'''
Given the participant's score sheet for your University Sports Day, you are required to find the runner-up score. You have scores. Store them in a list and find the score of the runner-up.
Sample input: [2, 3, 6, 6, 5]
Sample output: 5
Explanation: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.

'''

scores = [2, 3, 6, 6, 5]

max_score = max(scores)

while max_score in scores:
    scores.remove(max_score)

runner_up_score = max(scores)

print("Runner-up score is:", runner_up_score)

'''
You have a record of n students. Each record contains the student's name, and their percent marks in Math, Physics and Chemistry. The marks can be floating values. You are required to save the record in a dictionary data type.
Student's name is the key. Marks stored in a list is the value. The user enters a student's name. Output the average percentage marks obtained by that student.
Formula: (sum of marks) / (no of subjects)
Sample input: { "Krishna":
[67, 68, 69],
"Arjun":
[70, 98, 63),
"Malika":
[52, 56, 60]}
Sample output:
Enter a name: Malika
Average percentage mark:
56
Explanation:
Marks for Malika are [52, 56, 60] whose average is (52 + 56 + 60) / 3 =>56
'''

student_marks = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

name = input("Enter a name: ")

marks = student_marks.get(name)

if marks:
    average = sum(marks) / len(marks)
    print("Average percentage mark:")
    print(int(average)) 
else:
    print("Student not found.")


'''
Given a string of n words, help Alex to find out how many times his name appears in the string.
Constraint: 1 <= n <= 200
Sample input: Hi Alex WelcomeAlex Bye Alex.
Sample output: 3
Explanation: Alex name appears 3 times in the string. Hi Alex WelcomeAlex Bye Alex.
'''

# Step 1: Take the input string
text = input("Enter the string: ")

# Step 2: Count how many times 'Alex' appears
count = text.count("Alex")

# Step 3: Display the result
print("Number of times 'Alex' appears:", count)
