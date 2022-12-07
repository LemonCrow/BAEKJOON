starNum = int(input())
num = 0
jNum = -1
for i in range(starNum * 2):
    if starNum - i <= 0:
        num += 1
        jNum -= 2
    else:
        num = starNum - i
        jNum += 2
    for j in range(num - 1):
        print(" ", end="")
    for j in range(jNum):
        print("*", end="")
    print()
