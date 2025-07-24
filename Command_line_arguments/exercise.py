# 1. Accept Two Numbers and Display Their Sum

import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

total = num1 + num2
print("Sum:", total)

# 2. Accept a Welcome Message and Display File Name with Message

import sys

file_name = sys.argv[0]

message = sys.argv[1]

print("File name:", file_name)
print("Welcome message:", message)

# 3. Accept 10 Numbers and Calculate Sum of Prime Numbers

import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

numbers = list(map(int, sys.argv[1:]))

if len(numbers) != 10:
    print("Please enter exactly 10 numbers.")
else:
    prime_sum = sum(num for num in numbers if is_prime(num))
    print("Sum of prime numbers:", prime_sum)
