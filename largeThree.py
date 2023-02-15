a,b,c= map(int,(input().split()))

if a>b and a>c:
    print(a," is Largest among three.")
elif b>a and b>c:
    print(b," is Largest among three.")
else:
    print(c," is Largest among three.")

