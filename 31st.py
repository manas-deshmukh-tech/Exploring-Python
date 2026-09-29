n = int(input("Enter Number: "))
a = [0] * n

for i in range(n):
    a[i] = int(input("Enter number: "))

largest = a[0]
smallest = a[0]

for i in range(1, n):
    if a[i] > largest:
        largest = a[i]

    if a[i] < smallest:
        smallest = a[i]

second_largest = smallest
second_smallest = largest

for i in range(n):
    if a[i] > second_largest and a[i] != largest:
        second_largest = a[i]

    if a[i] < second_smallest and a[i] != smallest:
        second_smallest = a[i]

print("Largest =", largest)
print("Second Largest =", second_largest)
print("Smallest =", smallest)
print("Second Smallest =", second_smallest)