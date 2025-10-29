# Question 16 (b)
# Examination Number:
# Python program to find the median of a list of values

# MY COMMENTS -------Initialise a list of integers

#Initialise a list of numbers
numbers = [5, 2, 8, 3, 9]      # Currently using an odd example
#numbers = []
if not numbers:
    print("Error: The list of results is empty.")
# Display the list
print("Original list:", numbers)
# Sort the list
numbers.sort()

# Display the sorted list
print("Sorted list:", numbers)

# Find the number of elements in the list
length = len(numbers)

# Check if length is odd or even
if length % 2 == 1:
    # Odd case: median is the middle element
    median = numbers[length // 2]
else:
    # Even case: median is the mean of the two middle elements
    middle1 = numbers[length // 2 - 1]
    middle2 = numbers[length // 2]
    median = (middle1 + middle2) / 2


# Display the median
print("Median:", median)
