import random

# Generate a list of 5 random floating-point numbers between 0 and 10
numbers = [random.uniform(0, 10) for _ in range(5)]

# Display the generated list
print("Generated numbers:", numbers)

# Calculate and print the minimum and maximum values
print("Minimum value:", min(numbers))
print("Maximum value:", max(numbers))
