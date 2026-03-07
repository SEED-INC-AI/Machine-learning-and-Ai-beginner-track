# Exercise 1: Type Checking
numbers = [25, 19.99, "hello", True, None]
# Print the type of each value
for i in numbers:
    print(f"{i} {type(i)}")

# Exercise 2: Type Conversion
# Convert these to appropriate types:
age_str = "30"
int(age_str)
price = 99.99
is_valid = "True"
bool(is_valid)

# Exercise 3: ML Data Setup
accuracy = 0.99
samples = 63
dataset_name = "intership"
training_complete = False

# Solution 4: Validation
def validate_probability(value):
    return 0 <= value <= 1

for val in [0.5, -0.1, 1.5, 0, 1]:
    print(f"{val}: {validate_probability(val)}")