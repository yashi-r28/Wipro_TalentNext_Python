# 1. Read entire content from a .txt file and display to the user
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)


# 2. Read first n lines from a .txt file (get n from user):

n = int(input("Enter the number of lines to read: "))
with open("sample.txt", "r") as file:
    for i in range(n):
        line = file.readline()
        if not line:
            break
        print(line.strip())

# 3. Accept input from user and append it to a .txt file:

text = input("Enter text to append: ")
with open("sample.txt", "a") as file:
    file.write(text + "\n")
print("Text appended successfully.")


# 4. Read contents from a .txt file line by line and store each line into a list:

with open("sample.txt", "r") as file:
    lines = file.readlines()

line_list = [line.strip() for line in lines]
print("Lines in list format:\n", line_list)


# 5. Find the longest word from the .txt file contents (only one longest word):

with open("sample.txt", "r") as file:
    words = file.read().split()

longest = max(words, key=len)
print("Longest word in file is:", longest)


# 6. Count the frequency of a user-entered word in a .txt file:

word_to_count = input("Enter the word to count: ").lower()

with open("sample.txt", "r") as file:
    content = file.read().lower()
    words = content.split()

count = words.count(word_to_count)
print(f"The word '{word_to_count}' appears {count} times in the file.")



