file = open('/Users/linushohne/PycharmProjects/AdventOfCode2023/Day2/Puzzle')

lines = file.readlines()
print(lines)
answer = 0


def createsubgames(string, index):
    g = string.find(':') + 2

    while True:
        e = string.find(';', g) + 1
        if e == 0:
            subString = string[g:]
        else:
            subString = string[g:e]
        g = e + 1

        colorcount = 0
        for index, char in enumerate(subString):
            if char.isdigit():
                colorcount = int(str(colorcount) + str(char))

            if char == ',' or char == ';':
                colorcount = 0

            if char == ' ':
                color_type = subString[index + 1]
                match color_type:
                    case 'r':
                        if int(colorcount) > 12:
                            return False
                    case 'g':
                        if int(colorcount) > 13:
                            return False
                    case 'b':
                        if int(colorcount) > 14:
                            return False
        if e < 1:
            return True



for index, string in enumerate(lines):
    if createsubgames(string, index):
        answer += index + 1
        print(index + 1)

print('------------')
print(answer)
