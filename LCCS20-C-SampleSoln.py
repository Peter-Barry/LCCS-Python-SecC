# Question 16(c)
# Examination Number:
def find_nth_largest(n,list_of_values):
    list_of_values.sort()
    return list_of_values[n]

bmi_values = [24, 19, 33, 35, 27, 18, 15, 33, 35, 23, 32, 23]
obese_count = 0
for count in range(len(bmi_values)-1):
    if bmi_values[count] >=30:
        obese_count +=1
    
print("Obese ", obese_count)


# Sort the list in ascending order
bmi_values.sort()

# The largest value is the last element in the sorted list
largest = bmi_values[-1]

# The second largest value is the second-to-last element in the sorted list
second_largest = bmi_values[-3]

# Display the results
print(bmi_values)
print("Largest value:", largest)
print("Second largest value:", second_largest)
print("Finding",find_nth_largest(4,bmi_values))
