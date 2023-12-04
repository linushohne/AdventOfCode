file = open('/Users/linushohne/PycharmProjects/AdventOfCode2023/Day3/Puzzle')

lines = file.readlines()
print(lines)
sol = 0

def isSymbol(char):
    if char != '.' and not char.isdigit():
        return True
    else:
        return False
def checkForPart(firstdigit, lastdigit, line):
    line_length = len(lines[line])-1
    for i in range(firstdigit, lastdigit + 1):
        if 0 <= i - 1 < line_length and isSymbol(lines[line][i - 1]):
            return True
        elif 0 <= i + 1 < line_length and isSymbol(lines[line][i + 1]):
            return True
        elif 0 <= line + 1 < len(lines) and 0 <= i < line_length and isSymbol(lines[line + 1][i]):
            return True
        elif 0 <= line + 1 < len(lines) and 0 <= i - 1 < line_length and isSymbol(lines[line + 1][i - 1]):
            return True
        elif 0 <= line + 1 < len(lines) and 0 <= i + 1 < line_length and isSymbol(lines[line + 1][i + 1]):
            return True
        elif 0 <= line - 1 < len(lines) and 0 <= i < line_length and isSymbol(lines[line - 1][i]):
            return True
        elif 0 <= line - 1 < len(lines) and 0 <= i + 1 < line_length and isSymbol(lines[line - 1][i + 1]):
            return True
        elif 0 <= line - 1 < len(lines) and 0 <= i - 1 < line_length and isSymbol(lines[line - 1][i - 1]):
            return True
    return False

def findNumbers (string, line):
    firstdigit = -1
    lastdigit = -1
    sum = 0
    for index, char in enumerate(string):
        if char.isdigit():
            if firstdigit == -1:
                firstdigit = index
            lastdigit = index
        else:
            if firstdigit != -1 and checkForPart(firstdigit, lastdigit, line):
                sum += int(string[firstdigit:lastdigit + 1])
                print(string[firstdigit:lastdigit + 1])
            firstdigit = -1
            lastdigit = -1
    return sum


for index, line in enumerate(lines):
    sol += findNumbers(line, index)
print(sol)