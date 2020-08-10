def square_digits(num):
    num = str(num)
    result = ''
    for char in num:
        result += str(int(char)**2)
    return int(result)
