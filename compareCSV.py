with open('first.csv','r') as first, open('second.csv','r') as second:
    f1 = first.readlines()
    f2 = second.readlines()

for line in f1:
    if line not in f2:
        print(line)

for line in f2:
    if line not in f1:
        print(line)
        