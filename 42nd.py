n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for s in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print(chr(97 + j), end=" ")
    print()