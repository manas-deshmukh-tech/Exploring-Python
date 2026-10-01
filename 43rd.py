n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for s in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        if i == 1 or i == n or j == 0 or j == 2 * i - 2:
            print(chr(65 + j), end=" ")
        else:
            print(" ", end=" ")
    print()