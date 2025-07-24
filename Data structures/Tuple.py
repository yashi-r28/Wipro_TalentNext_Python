# 1. Print the 4th element from first and 4th from last in a tuple
t = (10, 20, 30, 40, 50, 60, 70, 80)
print("4th element from start:", t[3])
print("4th element from end:", t[-4])

# 2. Check whether an element exists in a tuple or not
t = (1, 2, 3, 4, 5)
element = int(input("Enter element to search: "))
if element in t:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")

# 3. Convert a list into a tuple
lst = [10, 20, 30, 40]
t = tuple(lst)
print("Converted Tuple:", t)

# 4. Find the index of an item in a tuple
t = (10, 20, 30, 40, 50)
item = int(input("Enter item to find index: "))
if item in t:
    print("Index of item:", t.index(item))
else:
    print("Item not found in tuple.")

# 5. Replace last value of tuples in a list to 100
lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
updated_list = [t[:-1] + (100,) for t in lst]
print("Updated List:", updated_list)
