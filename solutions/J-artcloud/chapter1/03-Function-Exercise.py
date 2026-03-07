# 03-Functions-Exercises.py
# Exercise 1: Basic Function
# Write a function to calculate area of circle
# area = pi * r^2
import math  
def circle_area(radius):
    area = math.pi * (radius**2)
    return area

# Exercise 2: Text Processing Function
# Write a function that cleans text:
# - strip whitespace
# - convert to lowercase
# - remove punctuation

def clean_text(text): 
    import string
    clean_text = text.strip()
    lowercase_text = text.lower()
    text_unpuct = text.translate(str.maketrans('', '', string.punctuation))
    print(clean_text)
    print(lowercase_text)
    print(text_unpuct)
    
# Exercise 3: ML Preprocessing Function
# Normalize a list of values to 0-1 range

def normalize_list(values):
    min_value = min(values)
    max_value = max(values)
    avg_value = max_value - min_value
    normalize = []
    for value in values:
        normalize.append((value - min_value)/avg_value)
    return normalize
    pass

# Exercise 4: Validation Function
# Check if email is valid (contains @)

def is_valid_email(email):
    if '@' in email:
        return 'valid email'
    pass

# Test your functions
print(circle_area(5))
print(clean_text("  HELLO WORLD!!!  "))
print(normalize_list([10, 20, 30, 40]))
print(is_valid_email("user@example.com"))
