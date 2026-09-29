n = int(input("Enter Number: "))
a = [0] * n
for i in range(n):
    a[i] = int(input("Enter number: "))
print("Original array:", a)
print("Reverse array:")
for i in range(n - 1, -1, -1):
    print(a[i], end=" ")