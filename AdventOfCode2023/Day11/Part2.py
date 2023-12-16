import numpy
import numpy as np

P = open("/Users/linushohne/PycharmProjects/AdventOfCode/AdventOfCode2023/Day11/Puzzle")

lines = P.read().strip().split("\n")

grid_array = [list(line) for line in lines]

galaxy_count = 1
for i, line in enumerate(grid_array):
    for ix, char in enumerate(line):
        if char == ".":
            grid_array[i][ix] = 0
        else:
            grid_array[i][ix] = galaxy_count
            galaxy_count += 1

grid = numpy.array(grid_array)

c = grid.sum(axis=0)
r = grid.sum(axis=1)

mill_c = []
mill_r = []

for i, x in enumerate(c):
    if x == 0:
        mill_c.append(i)

for i, x in enumerate(r):
    if x == 0:
        mill_r.append(i)



def check_mill(match, galaxy):
    add = 0
    for i in mill_c:
        if galaxy[1][0] < i < match[1][0] or galaxy[1][0] > i > match[1][0]:
            add += 999999

    for i in mill_r:
        if galaxy[0][0] < i < match[0][0] or galaxy[0][0] > i > match[0][0]:
            add += 999999

    return add


way = 0
cur_galaxy = 1

while cur_galaxy < galaxy_count:
    galaxy = np.where(grid == cur_galaxy)
    for i in range(cur_galaxy + 1, galaxy_count):
        match = np.where(grid == i)
        way += abs(match[0][0] - galaxy[0][0]) + abs(match[1][0] - galaxy[1][0]) + check_mill(match, galaxy)
    cur_galaxy += 1

print(way)
