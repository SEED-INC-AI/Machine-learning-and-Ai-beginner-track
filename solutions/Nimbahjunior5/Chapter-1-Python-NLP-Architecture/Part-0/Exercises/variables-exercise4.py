def validate_probability(value):
    # Check if the value is between 0 and 1 inclusive
    if 0 <= value <= 1:
        return True
    else:
        return False

# Test your function
test_values = [0.5, -0.1, 1.5, 0, 1]

for val in test_values:
    result = validate_probability(val)
    print(f"{val}: {result}")