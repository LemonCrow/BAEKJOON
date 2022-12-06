starNum = int(input())

for i in reversed(range(starNum)):
    for j in range(starNum - (i+1)):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print()