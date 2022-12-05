starNum = int(input())

for i in reversed(range(starNum+1)):
    for j in range(i):
        print("*", end="")
    print()