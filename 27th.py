n = int(input("Enter a number: "))
flag = 0
if n <= 1:
    flag = 1
else:
    for i in range(2, (n//2)+1):
        if n % i == 0:
            flag = 1
            break
if flag == 0:
    print("Prime")
else:
    print("Not Prime")