punctuations = """!@#$%^&*()_-{}[];:'"<>,./?|\`~*"""

string = input()

result=""

for char in string:
    if char not in punctuations:
        result = result + char

print(result)