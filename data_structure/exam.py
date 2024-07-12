# What is the output of the following code?

"""
def get_odd_number(numbers):
    odd_number = [num for num in numbers if num % 2 == 1]
    return odd_number


l1 = [0, 1, 2, 3, 4, 5]
print(get_odd_number(l1))"""

"""What is the meaning of s[::-1] ?"""

#What is the output of the following code?

"""
def reverse_string(strings):
    reversed_strings = [s[::1] for s in strings]
    return reversed_strings


str_list_1 = ["Hello", "Python", "Django"]
print(reverse_string(str_list_1))"""


# What is the output of the following code?


"""def merge_dicts(dict1, dict2):
    merged = dict2.copy()
    merged.update(dict1)
    return merged


dict1 = {'a':1, 'b':2}
dict2 = {'b':3, 'c': 4}
print(merge_dicts(dict1, dict2))
"""

# What is the output of the following code if we pass the value of print function is "
#num(4**2) " ?


"""num = lambda l:l*l
print(num(4**2))"""

# Which are mutable in Python?

"""
List

Dictionary
both 
none
"""

# What is the __init__() method?


# What is the output of the following code? [Note: Print the output by yourself]


class Data:
    def __init__(self, id):
        self.id = id
        id = 10


data = Data(20)

print(Data(20))

"""
syntaxt error

10
20 
none
"""

# How to define an initializer method in python?