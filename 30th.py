n = int(input("Enter Number: "))
a = [0] * n
sum = 0
for i in range(n):
    a[i] = int(input("Enter number: "))
    sum = sum + a[i]
print("Sum =", sum)