from collections import Counter

file = open('/Users/linushohne/PycharmProjects/AdventOfCode2023/Day4/Puzzle')
# file = open ('/Users/linushohne/PycharmProjects/AdventOfCode2023/Day4/testPuzzel')

lines = file.readlines()

sol = 0


def extractNumbers(string):
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
            if win == 0:
                win = 1
            else:
                win *= 2

    return win


for line in lines:
    sol += extractNumbers(line[9:])

print(sol)
