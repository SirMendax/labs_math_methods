
import math

def find_next_square(sq):
    number = math.sqrt(sq)
    if number.is_integer() == True:
        return int((number+1)**2)
    else:
        return -1
