n = int(input("Enter Number: "))
a = [0] * n

for i in range(n):
    a[i] = int(input("Enter number: "))
search = int(input("Enter number to search: "))
found = 0
for i in range(n):
    if a[i] == search:
        print("Number is present")
        print("Position =", i)
        found = 1
        break
if found == 0:
    print("Number is not present")