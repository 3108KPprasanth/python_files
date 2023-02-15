string = input()

words = [word for word in string.split()]

words.sort()

print("The sorted words are:")
for word in words:
    print(word)