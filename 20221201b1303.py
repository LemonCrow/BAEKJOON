import copy

N, M = input().split()

N = int(N)
M = int(M)
changeNumW = 1
changeNumB = 2
# W = True B = False

Array = [[0 for j in range(N)] for i in range(M)]

for i in range(M):
    Array[i] = list(input())

subArray = copy.deepcopy(Array)

if Array[0][0] == "W":
    isSame = True
else:
    isSame = False

for i in range(M):
    for j in range(N):
        if j > 0:
            if Array[i][j] == Array[i][j - 1]:
                if Array[i][j] == 'W':
                    if isSame != True:
                        isSame = True
                        changeNumW += 2
                    subArray[i][j] = subArray[i][j - 1] = changeNumW
                else:
                    if isSame != False:
                        isSame = False
                        changeNumB += 2
                    subArray[i][j] = subArray[i][j - 1] = changeNumB
        elif j > (N-1):
            if Array[i][j] == Array[i][j + 1]:
                if Array[i][j] == 'W':
                    if isSame != True:
                        isSame = True
                        changeNumW += 2
                    subArray[i][j] = subArray[i][j + 1] = changeNumW
                else:
                    if isSame != False:
                        isSame = False
                        changeNumB += 2
                    subArray[i][j] = subArray[i][j + 1] = changeNumB
        if i > 0:
            if Array[i][j] == Array[i - 1][j]:
                if Array[i][j] == 'W':
                    if isSame != True:
                        isSame = True
                        changeNumW += 2
                    subArray[i][j] = subArray[i - 1][j] = changeNumW
                else:
                    if isSame != False:
                        isSame = False
                        changeNumB += 2
                    subArray[i][j] = subArray[i - 1][j] = changeNumB
        elif i > (M-1):
            if Array[i][j] == Array[i + 1][j]:
                if Array[i][j] == 'W':
                    if isSame != True:
                        isSame = True
                        changeNumW += 2
                    subArray[i][j] = subArray[i][j + 1] = changeNumW
                else:
                    if isSame != False:
                        isSame = False
                        changeNumB += 2
                    subArray[i][j] = subArray[i][j + 1] = changeNumB


finalNum = changeNumW if changeNumW >= changeNumB else changeNumB

countW = countB = countNum = changeNumB = changeNumW = 0


for i in range(1, finalNum + 1):
    for j in range(M):
        countNum += subArray[j].count(i)
    if i % 2 != 0:
        changeNumW += countNum * countNum
    else:
        changeNumB += countNum * countNum
    countNum = 0

for i in range(M):
    countW += subArray[i].count('W')
    countB += subArray[i].count('B')

changeNumW += countW
changeNumB += countB

print(changeNumW, changeNumB)