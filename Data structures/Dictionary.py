# 1. Add a key and value to a dictionary
sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print("Updated Dictionary:", sample_dict)

# 2. Concatenate dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dict = {}
for d in (dic1, dic2, dic3):
    new_dict.update(d)
print("Concatenated Dictionary:", new_dict)

# 3. Check if a key exists in a dictionary
d = {1: 'a', 2: 'b', 3: 'c'}
key_to_check = 2
if key_to_check in d:
    print(f"Key {key_to_check} exists in the dictionary.")
else:
    print(f"Key {key_to_check} does not exist.")

# 4. Iterate and print keys, values, both
print("Keys:")
for k in d:
    print(k)

print("Values:")
for v in d.values():
    print(v)

print("Key-Value Pairs:")
for k, v in d.items():
    print(k, ":", v)

# 5. Dictionary of squares from 1 to 15
squares = {}
for i in range(1, 16):
    squares[i] = i ** 2
print("Squares Dictionary:", squares)

# 6. Sum all values in a dictionary
value_sum = sum(squares.values())
print("Sum of all values:", value_sum)
