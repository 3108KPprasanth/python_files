original = input()
reverse = ''.join(reversed(original))
if original == reverse:
    print("Given string is Palindrome.")
else:
    print("Not Palindrome.")