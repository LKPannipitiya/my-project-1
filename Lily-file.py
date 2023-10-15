# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract_numbers(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply_numbers(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide_numbers(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

# Get the two numbers as input.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the results using the functions
sum_result = add_numbers(num1, num2)
difference_result = subtract_numbers(num1, num2)
product_result = multiply_numbers(num1, num2)
division_result = divide_numbers(num1, num2)

# Print the results
print("The sum is:", sum_result)
print("The difference is:", difference_result)
print("The product is:", product_result)
print("The division result is:", division_result)
