starNum = int(input())
num = 0
for i in reversed(range(starNum+1)):
    for j in range(starNum - i):
        print(" ", end="")
    for j in range(i * 2 - 1):
        print("*", end="")
    num += 1
    print()
