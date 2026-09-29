n = int(input("Enter Number: "))
a = [0] * n
even = 0
odd = 0

for i in range(n):
    a[i] = int(input("Enter number: "))
    if a[i] % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even elements =", even)
print("Odd elements =", odd)