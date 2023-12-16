P = open("/Users/linushohne/PycharmProjects/AdventOfCode/AdventOfCode2023/Day10/Puzzle")

lines = P.readlines()

grid_array = [list(line) for line in lines]

## Start = 118,63

sol = 0
cur = (117, 63)
prev = (118, 63)

def find_next(next):
    cur = next[0]
    prev = next[1]
    cur_pipe = grid_array[cur[0]][cur[1]]

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
        sol += 1
        print(next)
        next = find_next(next)

print(sol/2)




