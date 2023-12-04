file = open('/Users/linushohne/PycharmProjects/AdventOfCode2023/Day2/Puzzle')

lines = file.readlines()
print(lines)
answer = 0


def createsubgames(string, index):
    g = string.find(':') + 2
    red = 0
    green = 0
    blue = 0

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
                        if int(colorcount) > red:
                            red = int(colorcount)
                    case 'g':
                        if int(colorcount) > green:
                            green = int(colorcount)
                    case 'b':
                        if int(colorcount) > blue:
                            blue = int(colorcount)
        if e == 0:
            return green * red * blue



for index, string in enumerate(lines):
    answer += createsubgames(string, index)

print('------------')
print(answer)
