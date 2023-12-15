import re

D = open('/Users/linushohne/PycharmProjects/AdventOfCode/AdventOfCode2023/Day6/Puzzel')

lines = D.readlines()

time = ""
distance = ""

times = re.findall(r'\d+', lines[0])
distances = re.findall(r'\d+', lines[1])

for i in times:
    time += i

for i in distances:
    distance += i



sol = 1



x = 0
wins = []

b = False
c = False

while b == False:
    x += 1
    if int(distance) < (int(time) - x) * x:
        if c == False:
            c = True
        wins.append(x)

    elif c == True:
        b = True

sol *= len(wins)

print(sol)

