import re

D = open('/Users/linushohne/PycharmProjects/AdventOfCode/AdventOfCode2023/Day9/Puzzle')

lines = D.readlines()

sol = 0


for l in lines:
    x = []
    x.append([int(num) for num in l.split()])

    while all(z == 0 for z in x[-1]) == False:
        y = []
        for i in range(len(x[-1])-1):
            y.append(int(x[-1][i+1]) - int(x[-1][i]))

        x.append(y)

    def getsum(index):
        if all(z == 0 for z in x[index]):
            return 0
        else:
            return x[index][0] - getsum(index + 1)

    print(x)
    sol += x[0][0] - getsum(1)





print(sol)
