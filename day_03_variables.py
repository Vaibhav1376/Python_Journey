# Day 3: Variables and Assignment
# This script is my reference for Python variable naming rules.

# --- Rule 1: Variables can only contain letters, numbers, and underscores. ---
# Good examples:
my_variable_1 = "This is correct"
user_age = 19
user_location_pune = True

# --- Rule 2: Variable names cannot start with a number. ---
# This would cause an error: 2_users = "Vaibhav"

# --- Rule 3: Spaces are not allowed. Use underscores instead (snake_case). ---
# Good example:
user_first_name = "Vaibhav"
# Bad example (would cause an error): user first name = "Vaibhav"

# --- Rule 4: Variable names are case-sensitive. ---
# 'age', 'Age', and 'AGE' are three different variables.
age = 19
Age = 20
AGE = 21

print("--- Variable Test ---")
print("User's first name is:", user_first_name)
print("Is user in Pune?", user_location_pune)
print("The three different age variables are:", age, Age, AGE)