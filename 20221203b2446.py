starNum = int(input())

for i in range(starNum):
    for j in range(i + 1):
        print("*", end="")
    print()