import math


def solution(area):
    # Your code here
    number = area
    result = []
    max_square = 2
    sum_of_max_square = 0
    while max_square > 1 and number > 1:
        sq_root = int(math.sqrt(number))
        max_square = sq_root ** 2
        result.append(str(max_square))
        sum_of_max_square += max_square
        number -= max_square
    remainder = area - sum_of_max_square
    result += ['1'] * remainder
    print(','.join(result))
