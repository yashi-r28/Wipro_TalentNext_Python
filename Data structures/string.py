# Program 1: Count upper and lower case letters

def count_case_letters(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

# Program 2: Check palindrome

def is_palindrome(s):
    return s == s[::-1]

# Program 3: Return n copies of first 2 characters

def multiple_first_two(s):
    return s[:2] * len(s)

# Program 4: Remove 'x' from beginning and end

def remove_x(s):
    if s.startswith('x'):
        s = s[1:]
    if s.endswith('x'):
        s = s[:-1]
    return s

# Program 5: Return n repetitions of last n characters

def repeat_last_n(s, n):
    return s[-n:] * n

# Example test cases
if __name__ == "__main__":
    print("Program 1:")
    count_case_letters("Hello World")

    print("\nProgram 2:")
    print("madam is palindrome:", is_palindrome("madam"))
    print("hello is palindrome:", is_palindrome("hello"))

    print("\nProgram 3:")
    print(multiple_first_two("Wipro"))  # Output: WiWiWiWiWi

    print("\nProgram 4:")
    print(remove_x("xHix"))  # Output: Hi

    print("\nProgram 5:")
    print(repeat_last_n("Wipro", 3))  # Output: propropro
