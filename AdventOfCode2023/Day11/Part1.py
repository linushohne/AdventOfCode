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

k = np.zeros(len(grid))
z = 0
for i, b in enumerate(c):
    if b == 0:
        grid = np.insert(grid, i + z, k, axis=1)
        z += 1

l = np.zeros(len(grid[0]))
z = 0
for i, b in enumerate(r):
    if b == 0:
        grid = np.insert(grid, i + z, l, axis=0)
        z += 1

print(grid)

way = 0
cur_galaxy = 1


while cur_galaxy < galaxy_count:
    galaxy = np.where(grid == cur_galaxy)
    for i in range(cur_galaxy + 1, galaxy_count):
        match = np.where(grid == i)
        way += abs(match[0][0] - galaxy[0][0]) + abs(match[1][0] - galaxy[1][0])
    cur_galaxy += 1

print(way)
