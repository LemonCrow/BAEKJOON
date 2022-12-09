repoStudent = []

for i in range(28):
    repoStudent.append(int(input()))

repoStudent.sort()

for i in range(1, 31):
    if i not in repoStudent:
        print(i)
