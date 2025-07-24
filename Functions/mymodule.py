
def ispalindrome(name):
    if name == name[::-1]:
        print("Yes, it is a palindrome.")
    else:
        print("No, it is not a palindrome.")

def count_the_vowels(name):
    vowels = 'aeiouAEIOU'
    count = 0
    for letter in name:
        if letter in vowels:
            count += 1
    print("No of vowels:", count)

def frequency_of_letters(name):
    freq = {}
    for letter in name:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    
    print("Frequency of letters:")
    for letter in freq:
        print(f"{letter}-{freq[letter]}")