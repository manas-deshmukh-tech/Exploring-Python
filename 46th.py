#checking if array is sorted
def isSorted(num):
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            return False

    return True
print(isSorted([1, 2, 3, 4, 5]))
print(isSorted([1, 3, 2, 4, 5]))