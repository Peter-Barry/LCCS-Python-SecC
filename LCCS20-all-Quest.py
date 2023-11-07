# Question 16(a)
# Examination Number:

weight = int(input("Enter weight (in kilograms): "))
height = 180 # centimetres

bmi = weight / (height * height) * 10000
print("BMI is: ", bmi)

# Question 16(b)
# Examination Number:

# For this question it is useful to understand ...
# 1. randint(a, b) returns a random integer N such that a<=N<=b.
# 2. s.append(x) appends the element x to the end of list s.

from random import *

heights = [] # an empty list of heights
weights = [] # an empty list of weights

# Loop to build up the lists with random values
for count in range(10):
# a random integer between 150 and 210
    heights.append(randint(150, 210))
# a random integer between 50 and 130
    weights.append(randint(50, 130))

# Display the lists


# Question 16(c)
# Examination Number:

bmi_values = [24, 19, 33, 35, 27, 18, 15, 33, 35, 23, 32, 23]
