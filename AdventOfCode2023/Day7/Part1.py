import re
P = open('/Users/linushohne/PycharmProjects/AdventOfCode/AdventOfCode2023/Day7/Puzzle')

lines = P.readlines()

hands = []
win = 0


def get_val(char):
    if char == 'T':
        return 10.0
    elif char == 'J':
        return 1.0
    elif char == 'Q':
        return 12.0
    elif char == 'K':
        return 13.0
    elif char == 'A':
        return 14.0
    else:
        return float(char)

def get_pair(string):
    values = []
    values.append(len(re.findall(r'2', string)))
    values.append(len(re.findall(r'3', string)))
    values.append(len(re.findall(r'4', string)))
    values.append(len(re.findall(r'5', string)))
    values.append(len(re.findall(r'6', string)))
    values.append(len(re.findall(r'7', string)))
    values.append(len(re.findall(r'8', string)))
    values.append(len(re.findall(r'9', string)))
    values.append(len(re.findall(r'T', string)))
    values.append(len(re.findall(r'J', string)))
    values.append(len(re.findall(r'Q', string)))
    values.append(len(re.findall(r'K', string)))
    values.append(len(re.findall(r'A', string)))


    two = 0
    three = 0
    for i in values:
        if i >= 2:
            two += 1
        if i >= 3:
            three += 1

    if two >= 2 and three >= 1:
        return 3.5
    elif two >= 2:
        return 2.5

    return float(max(values))

for i in lines:

    p = re.split(r'\s+', i)

    cards = []
    for c in p[0]:
        cards.append(get_val(c))

    for i, c in enumerate(cards):
        cards[i] = get_val(c)

    print(cards)

    x = (get_pair(p[0]),)
    w = (float(p[1]),)
    hands.append(x + tuple(cards) + w)

hands.sort()

for i,v in enumerate(hands):
    win += (i + 1) * v[-1]



print(hands)
print(win)


