#nomer 2
a = 5

for i in range (a):
    for j in range ( a, 0, -1):
        if j > i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
