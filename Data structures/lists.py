# 1. Create a list of 5 integers and display the list items. Access individual elements through index.
list1 = [10, 20, 30, 40, 50]
print("List Items:", list1)
print("Access by index:")
for i in range(len(list1)):
    print(f"Index {i}: {list1[i]}")

# 2. Append a new item to the end of the list.
list1.append(60)
print("After appending 60:", list1)

# 3. Reverse the order of the items in the list.
list1.reverse()
print("Reversed list:", list1)

# 4. Print the number of occurrences of a specified element in a list.
element = 30
count = list1.count(element)
print(f"Number of occurrences of {element}: {count}")

# 5. Append the items of list1 to list2 in the front.
list2 = [100, 200]
combined_list = list1 + list2
print("List after appending list1 to the front of list2:", combined_list)

# 6. Insert a new item before the second element in an existing list.
new_item = 15
list1.insert(1, new_item)
print("After inserting 15 before the second element:", list1)

# 7. Remove the item from a specified index in a list.
index_to_remove = 2
if 0 <= index_to_remove < len(list1):
    removed_item = list1.pop(index_to_remove)
    print(f"After removing item at index {index_to_remove} ({removed_item}):", list1)
else:
    print("Invalid index to remove.")

# 8. Remove the first occurrence of a specified element from a list.
element_to_remove = 30
if element_to_remove in list1:
    list1.remove(element_to_remove)
    print(f"After removing first occurrence of {element_to_remove}:", list1)
else:
    print(f"Element {element_to_remove} not found in the list.")