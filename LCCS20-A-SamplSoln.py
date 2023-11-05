# Question 16(a)
# Examination Number:
#(v)
def display_intro():
    print("welcome to my BMI calculator")
#(i)Read Weight
display_intro()
weight = int(input("Enter weight (in kilograms): "))
#(ii) Input Height
height = int(input("Enter Height (in Centimeters:)")) #180 # centimetres
#(iii) Round
#bmi = round(weight / (height * height) * 10000,2)
#(iv) using pow 
bmi = round(weight / pow(height,2) * 10000,2)


print("BMI is: ", bmi)
#(vi)
if bmi < 18.5:
    print("Underwieght")
elif bmi >= 18.5 and bmi < 24.9:
    print("normal")
elif bmi >= 25 and bmi < 29.9:
    print("Overweight")
elif bmi >= 30:
    print("Obese")
else:
    Print()
    
    

