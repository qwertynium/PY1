from turtle import clear

with open('/Task1/Test/input.txt') as inp:
    a = inp.read().split()

a = [int(x) for x in a]
a.sort()
i = []
ch = 0
r = 0
l = 0
while r < len(a):
    if int(a[r]) - int(a[l]) == int(1):
        if len(i) == 0 and ch == 0:
            ch = 1
        ch += 1
        print("kjsdfklj")
        if len(a) - r == 1 and ch > len(i):
            i = a[int(r - ch - 1):int(r)]
    else:
        if ch > len(i):
            i = a[int(r - ch - 1):int(r)]
            ch = 0
        ch = 0
    l = r
    r += 1
print(i)
