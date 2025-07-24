# 1. Division with Exception Handling

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Result of division:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numeric values.")
except Exception as e:
    print("Unexpected error:", e)

# 2. Prime Number Checker with Input Validation

try:
    num = int(input("Enter a number: "))
    if num < 2:
        print("Not a prime number.")
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                print("Not a prime number.")
                break
        else:
            print("It is a prime number.")
except ValueError:
    print("Error: Please enter a valid integer.")

# 3. Read File in Title Case with Exception Handling

try:
    filename = input("Enter filename (with .txt extension): ")
    with open(filename, 'r') as file:
        content = file.read()
        print("\nFile Contents in Title Case:\n")
        print(content.title())
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Unexpected error:", e)

# 4. List Index and Positive/Negative Checker

numbers = [10, -5, 7, -3, 8, 0, -9, 4, -1, 12]

try:
    index = int(input("Enter an index (0 to 9): "))
    value = numbers[index]
    if value > 0:
        print(f"The number at index {index} is positive: {value}")
    elif value < 0:
        print(f"The number at index {index} is negative: {value}")
    else:
        print(f"The number at index {index} is zero.")
except IndexError:
    print("Error: Index out of range. Enter index between 0 and 9.")
except ValueError:
    print("Error: Please enter a valid integer.")


