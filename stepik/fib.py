def fib(n):
    fibNumberPrev, fibNumberCurrent = 0, 1
    for i in range(1, n):
        fibNumberPrev, fibNumberCurrent = fibNumberCurrent, fibNumberPrev + fibNumberCurrent
    return fibNumberCurrent

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
