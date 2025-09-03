# Day 4: Type Conversion and User Input
# This script demonstrates converting data types and handling user input.

print("--- Numeric Conversion ---")
# An integer can be converted to a float.
i = 42
print(f"Original integer: {i} (Type: {type(i)})")

f = float(i)
print(f"Converted to float: {f} (Type: {type(f)})")
print("") # Adding a blank line for readability

print("--- String to Integer Conversion ---")
string_value = "123"
print(f"Original string: '{string_value}' (Type: {type(string_value)})")

# The int() function converts a string to an integer
integer_value = int(string_value)
print(f"Converted to integer: {integer_value} (Type: {type(integer_value)})")

# We can now perform math on the converted number
calculation = integer_value + 1
print(f"Adding 1 to the integer results in: {calculation}")
print("")

print("--- User Input ---")
# The input() function always returns a string
name = input("Please enter your name: ")
print(f"Welcome to my journey, {name}!")