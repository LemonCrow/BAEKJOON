starNum = int(input())
num = 0
for i in range(1, starNum+1):
    for j in range(1, starNum - num):
        print(" ", end="")
    for j in range(i + num):
        print("*", end="")
    num += 1
    print()
