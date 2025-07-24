# 1. Remove a given item from the set
s = {1, 2, 3, 4, 5}
s.discard(3)  # removes 3 if present
print("Set after removing 3:", s)

# 2. Intersection of sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1.intersection(set2)
print("Intersection of sets:", intersection)

# 3. Union of sets
union = set1.union(set2)
print("Union of sets:", union)

# 4. Find the maximum and minimum value in a set
s = {10, 30, 5, 25, 100}
print("Maximum value in set:", max(s))
print("Minimum value in set:", min(s))
