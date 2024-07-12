"""Find Next Number


Problem Statement
Write a program where you will be given three numbers. You will have to find the next number.

Input
The input consists of three integer numbers.

Output
The output will be an integer number.

Constraints
0 ≤ |S| ≤ 109
Example:
Enter three numbers.

Input:"""

input = input("").split(" ") 
num1 = float(input[0])
num2 = float(input[1])
num3 = float(input[2])

num4 = int(num3 + (num2-num1))
print(num4)
