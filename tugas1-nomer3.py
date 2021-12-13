#nomer 3
a = 6

for i in range(a):
    for j in range(a-1, 0, -1):
        if j <= i:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()