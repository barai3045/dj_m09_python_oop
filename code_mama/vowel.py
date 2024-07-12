"""
Problem Statement
Write a program to check if there is a vowel in a string.

Input
The input consists of a string.

Output
Output will be the answer whether there is a vowel or not. If there is vowel it will print "The string contains a vowel.", otherwise it will print "The string does not contain any vowel."

Constraints
The program will terminate whenever it finds a vowel.
Example-1:
Enter a String"""



character = input("")  
  
# Creating a list of vowels  
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  

consonent =  False
for x in character:
    if x in vowels:  
        print(f"The string contains a vowel.")  
        consonent = False
        break
    else:
        consonent = True

if consonent:
    print(f"The string does not contain any vowel.")  
