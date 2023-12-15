import re

D = open('/Users/linushohne/PycharmProjects/AdventOfCode/AdventOfCode2023/Day6/Puzzel')

lines = D.readlines()

times = re.findall(r'\d+', lines[0])
distances = re.findall(r'\d+', lines[1])



sol = 1


for i in range(len(times)):
    x = 0
    wins = []

    b = False
    c = False

    while b == False:
        x += 1
        if int(distances[i]) < (int(times[i]) - x) * x:
            if c == False:
                c = True
            wins.append(x)
            print(x)
        elif c == True:
            b = True

    sol *= len(wins)
    print(len(wins))

print(sol)

