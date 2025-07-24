# 1. Function to return the sum of all numbers in a list

def sum_of_list(numbers):
    total = sum(numbers)
    return total

# Sample usage
sample_list = [8, 2, 3, 0, 7]
print("Sum:", sum_of_list(sample_list))  # Output: 20


# 2. Function to return the reverse of a string
def reverse_string(text):
    return text[::-1]

sample_text = "1234abcd"
print("Reversed string:", reverse_string(sample_text))  # Output: "dcba4321"

# 3. Function to calculate and return the factorial of a number

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print("Factorial:", factorial(5))

# 4. Function to count uppercase and lowercase letters in a string

def count_case_letters(text):
    upper_count = 0
    lower_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print("Uppercase letters:", upper_count)
    print("Lowercase letters:", lower_count)

count_case_letters("Hello World!")  

# 5. Function to print even numbers from a given list

def print_even_numbers(num_list):
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
    print("Even numbers:", even_numbers)

print_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])  

# 6. Function to check whether a number is prime

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Is 7 prime?", is_prime(7)) 
print("Is 10 prime?", is_prime(10)) 
