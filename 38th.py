n = 5
sp = n - 1

for i in range(1, n + 1):

    for s in range(0, sp):
        print(end=" ")

    for j in range(1, i + 1):
        print(j, end=" ")

    print()

    sp = sp - 1