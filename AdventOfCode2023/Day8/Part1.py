import re

P = open('/Users/linushohne/PycharmProjects/AdventOfCode/AdventOfCode2023/Day8/Puzzle')

lines = T.readlines()

nav = list(lines[0])

nodes = []
edgesL = []
edgesR = []

for l in lines[2:]:
    x = re.findall(r'[a-zA-Z]{3}', l)
    nodes.append(x[0])
    edgesL.append(x[1])
    edgesR.append(x[2])


node = "AAA"
n = 0
x = 0
while True:
    if n > len(nav)-2:
        n = 0
        print("Reset")

    if node == "ZZZ":
        break

    match = [x for x in nodes if node in x]

    if nav[n] == "L":
        node = edgesL[nodes.index(match[0])]
        print("Zu " + node)

    else:
        node = edgesR[nodes.index(match[0])]
        print("Zu " + node)

    n += 1
    x += 1

print(x)
print(nodes)