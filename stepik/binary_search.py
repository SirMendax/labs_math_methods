import sys
import math


def binary_search(list, element):
    count = len(list)-1
    i = 0
    while count >= i:
        m = math.floor(((i+count)/2))
        if list[m] == element:
            return m+1
        elif list[m] > element:
            count = m - 1
        else:
            i = m + 1
    return -1


def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *xs = next(reader)
    k, *queries = next(reader)
    for char in queries:
        print(binary_search(xs, char), end=" ")


if __name__ == "__main__":
    main()
