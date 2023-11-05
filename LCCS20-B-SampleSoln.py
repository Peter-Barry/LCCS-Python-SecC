# Examination Number:

# For this question it is useful to understand ...
# 1. randint(a, b) returns a random integer N such that a<=N<=b.
# 2. s.append(x) appends the element x to the end of list s.

from random import *

heights = [] # an empty list of heights
weights = [] # an empty list of weights
bmi_values = []
#(ii)
pairs = int(input("Enter the no of pairs "))

# Loop to build up the lists with random values
#(ii)
for count in range(0,pairs,1):
# a random integer between 150 and 210
    heights.append(randint(150, 210))
# a random integer between 50 and 130
    weights.append(randint(50, 130))
    

for count in range (pairs):

    bmi = round(weights[count] / pow(heights[count],2) * 10000,2)
    bmi_values.append(bmi)
    #bmi_values[count] = round(weights[count] / pow(heights[count],2) * 10000,2)
    
# (i) Display the lists
print("Heights: ",heights)
print("Weights: ",weights)
print("BMI_Valuse ",bmi_values)
