age_str = "30"
price = 99.99
is_valid = "True"

# Conversions
age_int = int(age_str)         # String to Integer
price_str = str(price)         # Float to String
valid_bool = is_valid == "True" # String to Boolean logic

print(f"Age: {type(age_int)}, Price: {type(price_str)}, Valid: {type(valid_bool)}")