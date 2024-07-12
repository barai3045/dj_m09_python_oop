"""BMI Calculator

Problem Statement
Write a program where user will give height(height) and weight(kg) and then BMI will be calculated.

Input
The input consists of two double numbers which are height(meter) and weight(kg).

Output
*if bmi < 18.5 print "Underweight" *if bmi >= 18.5 & bmi < 25.0 print "Normal weight" *if bmi >= 25.0 & bmi < 30.0 print "Overweight" *else print "Obese"

Constraints
0 ≤ |S| ≤ 109
Example:
Enter height and weight."""


input = input("").split(" ") 
height = float(input[0])
weight = float(input[1])
bmi = weight/height/height

print(f"BMI: {bmi:.2f}")
if bmi < 18.5:
    print(f"Underweight") 
elif bmi >= 18.5 and bmi < 25.0: 
    print(f"Normal weight") 
elif bmi >= 25.0 and bmi < 30.0: 
    print(f"Overweight")
else:
    print(f"Obese")
