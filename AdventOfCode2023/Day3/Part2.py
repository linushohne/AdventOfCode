file = open('/Users/linushohne/PycharmProjects/AdventOfCode2023/Day3/Puzzle')
#file = open ('/Users/linushohne/PycharmProjects/AdventOfCode2023/Day3/test puzzle')

lines = file.readlines()
print(lines)
sol = 0


def findNumber(line, pos):
    number = ''

    right_pos = pos
    while right_pos < len(lines[line]) and lines[line][right_pos].isdigit():
        number += lines[line][right_pos]
        right_pos += 1

    # Check if there are additional digits to the left of the current position
    left_pos = pos - 1
    while left_pos >= 0 and lines[line][left_pos].isdigit():
        number = lines[line][left_pos] + number
        left_pos -= 1

    print(number + '|' + str(line) + '|' + str(pos))
    return int(number) if number else 0

def checkForGear(i, line):
    line_length = len(lines[line]) - 1
    gearNums = []

    if 0 <= i - 1 < line_length and lines[line][i - 1].isdigit():
        gearNums.append(findNumber(line, i - 1))
    if 0 <= i + 1 < line_length and lines[line][i + 1].isdigit():
        gearNums.append(findNumber(line, i + 1))
    if 0 <= line + 1 < len(lines) and 0 <= i < line_length and lines[line + 1][i].isdigit():
        gearNums.append(findNumber(line + 1, i))
    if 0 <= line + 1 < len(lines) and 0 <= i - 1 < line_length and lines[line + 1][i - 1].isdigit():
        gearNums.append(findNumber(line + 1, i - 1))
    if 0 <= line + 1 < len(lines) and 0 <= i + 1 < line_length and lines[line + 1][i + 1].isdigit():
        gearNums.append(findNumber(line + 1, i + 1))
    if 0 <= line - 1 < len(lines) and 0 <= i < line_length and lines[line - 1][i].isdigit():
        gearNums.append(findNumber(line - 1, i))
    if 0 <= line - 1 < len(lines) and 0 <= i + 1 < line_length and lines[line - 1][i + 1].isdigit():
        gearNums.append(findNumber(line - 1, i + 1))
    if 0 <= line - 1 < len(lines) and 0 <= i - 1 < line_length and lines[line - 1][i - 1].isdigit():
        gearNums.append(findNumber(line - 1, i - 1))

    gearNums = list(dict.fromkeys(gearNums))

    if len(gearNums) == 2:
        return int(gearNums[0]) * int(gearNums[1])
    else:
        return 0



def findGears(string, line):
    sum = 0
    for index, char in enumerate(string):
        if char == '*':
             sum += checkForGear(index, line)
    return sum


for index, line in enumerate(lines):
    sol+= findGears(line, index)

print(sol)

