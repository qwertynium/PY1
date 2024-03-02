with open('Task3/Test/input.txt', 'r') as f:
    m=[]
    for row in f:
        m.append([int(x) for x in row.strip().split(" ")])

print(m)
a = [[1,12],[0,10],[0,10]]
max = 0

for i in range(len(a)):
    for j in range(len(a)):
        if a[i][1] >= a[j][0] and a[i][0] < a[j][1]:
            b = a[j][1] - a[i][0]
            if b > max:
                max = b
        elif a[i][1] >= a[j][1] and a[i][0] <= a[j][0]:
            b = a[i][1] - a[i][0]
            if b > max:
                max = b


print(max)