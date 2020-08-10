import math


def binary_search(array, item):
    low = 0
    high = len(array)-1

    while low <= high:
        mid = math.floor((low+high)/2)
        guess = array[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    res = binary_search([1, 3, 5, 7, 9, 12, 34, 56, 235, 6346, 124], 12)
    print(res)
