from collections import Counter

file = open('/Users/linushohne/PycharmProjects/AdventOfCode2023/Day4/Puzzle')
#file = open ('/Users/linushohne/PycharmProjects/AdventOfCode2023/Day4/testPuzzel')

lines = file.readlines()
countedLines = []

sol = 0


def addCards(win, index):
    i = 1
    while i <= win:
        if i + index <= len(countedLines):
            countedLines[index + i] += 1 * countedLines[index]
        i += 1


def extractNumbers(string, index):
    number = ''
    numbers = []
    win = 0
    for char in string:
        if char.isdigit():
            number += char
        else:
            if number:
                numbers.append(number)
                number = ''

    c = Counter(numbers)

    for i in c:
        if c[i] == 2:
            win += 1

    addCards(win, index)


for i in lines:
    countedLines.append(1)


for index, line in enumerate(lines):
    extractNumbers(line[9:], index)


print(sum(countedLines))