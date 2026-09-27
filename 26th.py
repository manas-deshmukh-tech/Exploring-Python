#Different Ways to print no from 1 to 10
#1 using for and range 
for i in range(1, 11):
    print(i)
#2 using while
i = 1
while i <= 10:
    print(i)
    i += 1 
#3 using recursion 
def numbers(i):
    if i > 10:
        return

    print(i)
    numbers(i + 1)

numbers(1)
#4 using function and for 
def print_numbers():
    for i in range(1, 11):
        print(i)

print_numbers()