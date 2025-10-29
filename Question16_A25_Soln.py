# Question 16 (a)
# Examination Number:
"""
def get_grade(result):
    grade = "Unsuccessful"
    
    if result >= 80:
        grade = "Distinction"
    elif result >= 65:
        grade = "Upper Merit"

    return grade
    """
def get_grade(result):
    if result >= 80:
        grade = "Distinction"
    elif result >= 65:
        grade = "Upper Merit"
    elif result >= 50:
        grade = "Lower Merit"
    elif result >= 40:
        grade = "Pass"
    else:
        grade = "Unsuccessful"
    return grade

# Calculate and display the mean of a list of results
results = [39,32,62,88,51,62,64,81,77] # Initialise the list
N = len(results) # Initialise N to the number of results
total = 0 # Initialise the running total to 0

# Loop N times
for i in range(N):
    total = total + results[i] # Running total

# Divide by the total number of results to give the mean
arithmetic_mean = total/9
# Q1
arithmetic_mean = round(total / 9, 2)
# Q2
arithmetic_mean = round(total / N, 2)

# Display the answer
print("The mean percentage mark is", arithmetic_mean)
#Q3
mean_grade = get_grade(arithmetic_mean)
print("The grade for the average result is", mean_grade)
#Q4
lowest_score = min(results)
highest_score = max(results)
print("The lowest score is", lowest_score)
print("The highest score is", highest_score)

#Q5
count_below_40 = sum(1 for score in results if score < 40)
count_50_to_79 = sum(1 for score in results if 50 <= score <= 79)

print("The number of scores below 40 is", count_below_40)
print("The number of scores between 50 and 79 inclusive is", count_50_to_79)

#Q6
# Find the longest run of consecutive increases
longest_run = []
current_run = [results[0]]

for i in range(1, len(results)):
    if results[i] > results[i-1]:
        current_run.append(results[i])
    else:
        if len(current_run) > len(longest_run):
            longest_run = current_run
        current_run = [results[i]]

# Check at the end in case the longest run is at the end
if len(current_run) > len(longest_run):
    longest_run = current_run

print("The longest run of result increases is", longest_run)

