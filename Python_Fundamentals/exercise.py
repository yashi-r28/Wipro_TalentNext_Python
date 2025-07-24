# Q1. Check if a number is Positive, Negative or Zero

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Q2. Check if a number is Odd or Even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q3. Check if two numbers have the same last digit

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % 10 == num2 % 10:
    print("True")
else:
    print("False")


# Q4. Print numbers from 1 to 10 in a row with tab space
for i in range(1, 11):
    print(i, end="\t")

# Q5. Print even numbers between 23 and 57, each on a new line
for i in range(23, 58):
    if i % 2 == 0:
        print(i)


# Q6. Check if a number is Prime
num = int(input("Enter a number: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")


# Q7. Print prime numbers between 10 and 99
for num in range(10, 100):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# Q8. Print the sum of all digits of a number
num = int(input("Enter a number: "))
sum_of_digits = 0

while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num = num // 10

print("Sum of digits:", sum_of_digits)


#  Q9. Reverse a number
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)


# Q10. Check if a number is Palindrome
num = int(input("Enter a number: "))
original_num = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original_num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")