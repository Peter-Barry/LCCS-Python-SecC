# Question 16(a)
# Examination Number:
from random import randint

print("Dice simulation and analysis program") # part (i)
results = []
frequencies = [0, 0, 0, 0, 0, 0]

# Generate 100 random values between 1 and 6 and append them to the results list
for i in range (100):
    throw_result = randint(1,6)
    results.append(throw_result)
# Start to build up a list of frequencies for each number thrown
    if throw_result == 1:
        frequencies[0] = frequencies[0] + 1
    elif throw_result == 2:
        frequencies[1] = frequencies[1] + 1
# part (iii) – start
    elif throw_result == 3:
        frequencies[2] = frequencies[2] + 1
    elif throw_result == 4:
        frequencies[3] = frequencies[3] + 1
    elif throw_result == 5:
        frequencies[4] = frequencies[4] + 1
    elif throw_result == 6:
        frequencies[5] = frequencies[5] + 1
# part (iii) - end

print()
#print("Results:",results) # part (iv)

print("Frequencies:", frequencies) # part (ii)

# part (v) - start
print()
print("Dice\tFrequency")
print("----\t---------")
for i in range(6):
    print(i+1,"\t",frequencies[i])

# part (vi) - start
print()
largest = max(frequencies)
print(frequencies.index(largest)+1, "was rolled most often -", largest, "times")

# part (vii)
# Horizontal Bar Chart ... nested loop
print()
for freq in frequencies:
    for i in range(freq):
        print("*", end="")
    print()