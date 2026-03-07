# 04-DataStructures-Exercises.py

# Exercise 1: List Operations
# Create a list of fruits and:
# - Add "mango"
# - Remove "apple"
# - Sort alphabetically
# - Print each with index
list_item = ['apple','banana','kiwi']
list_item.append('apple')
list_item.remove('mango')
list_item.sorted()
for index,item in enumerate(list_item):
    print(f'{index}: {item}')
    
    
# Exercise 2: Dictionary Creation
# Create student records:
student_data = [
    ("Alice", 25, 3.85),
    ("Bob", 23, 3.92),
    ("Charlie", 24, 3.45)
]
# Convert to list of dictionaries with keys: name, age, gpa
student_data = dict(student_data)
print(student_data)
# Exercise 3: Set Operations
# Given two sets of tags, find:
tags1 = {"python", "ml", "ai", "data"}
tags2 = {"python", "web", "data", "django"}
# - Common tags
common = tags1 & tags2
print(common)
# - Unique to tags1
print(tags1.unique())
# - All tags combined

# Exercise 4: Nested Data Structure
# Create a dictionary of ML models:
# Each model has: name, accuracy, parameters_count
# Perform operations on the structure

# Exercise 5: Data Deduplication
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unduplicate = set(data)
print(unduplicate)
# Remove duplicates and count occurrences
