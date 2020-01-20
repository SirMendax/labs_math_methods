import sys
def fib_mod(n, m):
    moduloArray = [0,1]
    for i in range(2, 6*m):
        buf = (moduloArray[i-1] + moduloArray[i-2]) % m
        moduloArray.append(buf)
        if (moduloArray[i-1] == 0 and moduloArray[i] == 1):
            num = n % (len(moduloArray)-2)
            return moduloArray[num]

def main():
    n, m = map(int, sys.stdin.read().split())
    res = fib_mod(n,m)
    print(str(res))


if __name__ == "__main__":
    main()
