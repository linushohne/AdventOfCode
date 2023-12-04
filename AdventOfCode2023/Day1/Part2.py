file = open('/Users/linushohne/PycharmProjects/pythonProject/Day1/Puzzle')
lines = file.readlines()
#lines = ["two2223344three"]
print(lines)
sum_var = 0
numberlines = list()

wordNumbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}



def getNums(string):
    numberline = ''
    numbersInLine = {}
    x = -1
    for index, char in enumerate(string):
        if char.isdigit():
            numbersInLine[index] = char
    for index, tuple in enumerate(wordNumbers):
        p = 0
        while True:
            s = string.find(list(wordNumbers.values())[index], p)
            if s >= 0:
                numbersInLine[s] = list(wordNumbers)[index]
                p = s + 1
            else:
                break

    sortedNums = dict(sorted(numbersInLine.items()))
    if len(list(sortedNums)) > 1:
        return int(str(list(sortedNums.values())[0]) + str(list(sortedNums.values())[len(list(sortedNums))-1]))
    else:
        return int(str(list(sortedNums.values())[0]) + str(list(sortedNums.values())[0]))


for i in lines:
    sum_var += getNums(i)



print(sum_var)


