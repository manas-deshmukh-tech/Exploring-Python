#count the number of digits in the factorial of a given number.
def digitInFactorial(n: int) -> int:
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    count = 0

    while fact > 0:
        count += 1
        fact = fact // 10
    return count
print(digitInFactorial(7))