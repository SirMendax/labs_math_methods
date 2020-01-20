import sys
def fib_digit(n):
    fibNumberPrev, fibNumberCurrent = 0, 1
    for i in range(1, n):
        fibNumberPrev, fibNumberCurrent = fibNumberCurrent % 10, fibNumberPrev + fibNumberCurrent
    return str(fibNumberCurrent)[-1]

def main():
    n = int(sys.stdin.read())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
