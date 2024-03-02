a = ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 2, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 3],
      [0, 0, 2, 1, 0, 0, 0, 1, 3, 0],
      [0, 2, 0, 0, 0, 0, 1, 0, 0, 0],
      [2, 0, 0, 0, 0, 1, 0, 0, 0, 0],
      [9, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

print(a)


def p(a):
    foundone = 0
    foundtwo = 0
    count = 0
    b = True
    # горизонталь
    for column in range(len(a)):
        for row in range(1, len(a[0])):
            if a[column][row - 1] == a[column][row] and a[column][row] != int(0):
                if count == int(0):
                    count = 1
                count += 1
                if count == int(5):
                    # print("решение тута есть точно не обманываю: qwerty " + str(a[column][row]))
                    if a[column][row] == int(1):
                        foundone += 1
                    else:
                        foundtwo += 1
            else:
                count = 0

    # вертикаль
    for row in range(len(a[0])):
        for column in range(len(a) - 1):
            if a[column][row] == a[column + 1][row] and a[column][row] != int(0):
                if count == int(0):
                    count = 1
                count += 1
                if count == int(5):
                    # print("решение тута есть точно не обманываю: qwerty " + str(a[column][row]))
                    if a[column][row] == int(1):
                        foundone += 1
                    else:
                        foundtwo += 1
            else:
                count = 0

    # диагональ(лево-право)
    column = 0
    k = 1
    row = len(a[0]) - k
    count = 0
    l = 0
    while b:
        if row == int(0) and column == int(len(a)-1):
            print(a[column][row])
            break
        if row < len(a[0]) - 1 and column < len(a) - 1:
            if a[column][row] == a[column + 1][row + 1] and a[column][row] != int(0):
                if count == int(0):
                    count = 1
                count += 1
                if count == int(5):
                    # print("решение тута есть точно не обманываю: (лево-право) " + str(a[column][row]))
                    if a[column][row] == int(1):
                        foundone += 1
                    else:
                        foundtwo += 1

            else:
                count = 0
            column += 1
            row += 1
        elif l == int(0):
            column = 0
            k += 1
            if len(a) - k == int(0):
                column = 0
                k = 0
                row = 0
                count = 0
                l = 1
            else:
                row = len(a) - k

        elif l == int(1):
            k += 1
            column = k
            row = 0
            if k != len(a):
                row = 0

    # диагональ(право-лево)
    column = 0
    k = 0
    row = int(len(a[0])) - 1
    count = 0
    l = 0
    b = True
    while b:
        if row == int(len(a) - 1) and column == int(len(a) - 1):
            print(a[column][row])
            break
        if row > 0 and column < len(a) - 1:
            if a[column][row] == a[column + 1][row - 1] and a[column][row] != int(0):
                if count == int(0):
                    count = 1
                count += 1
                if count == int(5):
                    # print("решение тута есть точно не обманываю:(право-лево) " + str(a[column][row]))
                    if a[column][row] == int(1):
                        foundone += 1
                    else:
                        foundtwo += 1
            else:
                count = 0
            column += 1
            row -= 1
        elif l == int(0):
            column = 0
            k += 1
            if len(a[0]) - k == int(0):
                b = True
                column = 0
                k = 0
                row = int(len(a[0])) - 1
                count = 0
                l = 1
            else:
                row = len(a[0]) - k

        elif l == int(1):
            k += 1
            column = k
            row = int(len(a[0])) - 1
            if k != len(a):
                row = int(len(a[0])) - 1

    if foundone == 0 and foundtwo == 0 or foundone >= 1 and foundtwo >= 1:
        return 1
    elif foundone >= 1:
        return 2
    else:
        return 3

c = p(a)
if int(c) == 1:
    print("Draw")
if int(c) == 2:
    print("Win 1")
if int(c) == 3:
    print("Win 2")
