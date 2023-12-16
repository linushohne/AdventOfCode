P = open("/Users/linushohne/PycharmProjects/AdventOfCode/AdventOfCode2023/Day10/Puzzle")

lines = P.readlines()

grid_array = [list(line) for line in lines]
map = [[" "] * len(grid_array[0]) for _ in range(len(grid_array))]

## Start = 118,63

sol = 0
cur = (117, 63)
prev = (118, 63)

def find_next(next):
    cur = next[0]
    prev = next[1]
    cur_pipe = grid_array[cur[0]][cur[1]]
    map[cur[0]][cur[1]] = cur_pipe

    match cur_pipe:
        case "|":
            if prev[0] < cur[0]:
                cur = (cur[0] + 1, cur[1])
            else:
                cur = (cur[0] - 1, cur[1])

        case "-":
            if prev[1] < cur[1]:
                cur = (cur[0], cur[1] + 1)
            else:
                cur = (cur[0], cur[1] - 1)

        case "L":
            if prev[0] == cur[0]:
                cur = (cur[0] - 1, cur[1])
            else:
                cur = (cur[0], cur[1] + 1)

        case "J":
            if prev[0] == cur[0]:
                cur = (cur[0] - 1, cur[1])
            else:
                cur = (cur[0], cur[1] - 1)
        case "7":
            if prev[0] == cur[0]:
                cur = (cur[0] + 1, cur[1])
            else:
                cur = (cur[0], cur[1] - 1)
        case "F":
            if prev[0] == cur[0]:
                cur = (cur[0] + 1, cur[1])
            else:
                cur = (cur[0], cur[1] + 1)
        case "S":
            return(-1)

    return (cur, next[0])


next = (cur, prev)

while True:
    if next == -1:
        print("complete")
        break
    else:
        next = find_next(next)


# using rey cast algorithm
def count_intersections(row, i):
    ints = ["|", "J", "L", "S"]  #S-Pipe = | in my case
    count = 0
    for char in row[:i]:
        if char in ints:
            count += 1

    return count


for i, row in enumerate(grid_array):
    for ix, char in enumerate(row):
        if map[i][ix] == " " and count_intersections(map[i], ix) % 2 == 1:
            sol += 1

for row in map:
    print(row)

print(sol)







