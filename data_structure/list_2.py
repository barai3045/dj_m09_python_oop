# write a function that takes a list of string and returns a new list with each string reversed
# ex: ["abc", "hello"] -> ["cba", "olleh"]

def reverse_string(strings):
    reverse_strings = [s[::-1] for s in strings]
    return reverse_strings

str_list = ["hello", "python", "django"]

print(reverse_string(str_list))