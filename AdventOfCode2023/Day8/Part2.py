import re
import math

P = open('/Users/linushohne/PycharmProjects/AdventOfCode/AdventOfCode2023/Day8/Puzzle')

lines = P.readlines()

nav = list(lines[0])


nodes = []
edgesL = []
edgesR = []

for l in lines[2:]:
    x = re.findall(r'\w{3}', l)
    nodes.append(x[0])
    edgesL.append(x[1])
    edgesR.append(x[2])

start_nodes = []


for i, n in enumerate(nodes):
    if re.match(r'\w{2}A', n):
        start_nodes.append(n)


cycles = []
for i in start_nodes:
    node = i
    n = 0
    x = 0
    while True:
        if n > len(nav)-2:
            n = 0

        if re.match(r'\w{2}Z', node) != None:
            break

        match = [x for x in nodes if node in x]

        if nav[n] == "L":
            node = edgesL[nodes.index(match[0])]

        else:
            node = edgesR[nodes.index(match[0])]
        n += 1
        x += 1
    cycles.append(x)
    print(x)

print(cycles)

print(math.lcm(*cycles))



