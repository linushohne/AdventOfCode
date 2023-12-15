import re
from datetime import datetime
import numpy as np

D = open('/Users/linushohne/PycharmProjects/AdventOfCode/AdventOfCode2023/Day5/Puzzle')
#D = open('/Users/linushohne/PycharmProjects/AdventOfCode/AdventOfCode2023/Day5/test_puzzle')

lines = D.readlines()


seed_target = re.findall(r'\d+', lines[0])
seed_nums = [int(num) for num in seed_target]


seeds = []
s = 1
while s < len(seed_nums):
    new_s = range(seed_nums[s-1], seed_nums[s] + seed_nums[s-1])
    seeds = np.concatenate((seeds, new_s), axis=None)
    s += 2




pattern = re.compile(r'\d+')


def set_map(begin, end):
    map = []
    for l in lines[begin:end + 1]:
        st = re.findall(pattern, l)
        s = [int(num) for num in st]
        map.append(s)
    return map


maps = []
map_begin = -1
map_end = -1
for i, l in enumerate(lines):
    if l[0].isdigit():
        if map_begin == -1:
            map_begin = i
        map_end = i

    elif map_begin != -1:
        maps.append(set_map(map_begin, map_end))
        map_begin = -1
        map_end = -1

if map_begin != -1:
    maps.append(set_map(map_begin, map_end))

for index, map in enumerate(maps):
    for i, seed in enumerate(seeds):
        for m in map:
            if (m[1] + m[2]) > seed and seed >= m[1]:
                seeds[i] = m[0] + (seed - m[1])

print(min(seeds))

print('----------------------------------')
print(datetime.now())