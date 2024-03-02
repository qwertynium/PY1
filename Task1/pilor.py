with open('Task1/Test/input.txt', 'r') as f:
    k = [int(x) for x in f.read().strip().split(" ")]
k.sort()

a = k

r = 0
l = 0
i = []
ch = 0
if int(len(a)) == int(1):
    with open("Task1/Test/output.txt", "w") as output:
        output.write(str(a))
elif int(len(a)) == int(0):
    with open("Task1/Test/output.txt", "w") as output:
        output.write("Enter the value in the file input.txt")
else:
    while r < len(a):
        if int(a[r]) - int(a[l]) == int(1):
            if ch == 0:
                ch += 1
            ch += 1
            if int(len(a)) - int(r) == int(1) and ch > len(i):
                i = a[int(r - ch + 1):int(r + 1)]
        else:
            if ch > len(i):
                i = a[int(r - ch):int(r)]
                ch = 0
            ch = 0
        l = r
        r += 1

    with open("Task1/Test/output.txt", "w") as output:
        output.write(str(i))
