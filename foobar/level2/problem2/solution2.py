from fractions import Fraction


def construct_numerator_mid(mid_pegs):
    total = 0
    for i in range(0, len(mid_pegs)):
        if i % 2 == 0:
            total += 2 * mid_pegs[i]
        else:
            total -= 2 * mid_pegs[i]
    return total


def construct_numerator(pegs):
    first = -pegs[0]
    last = ((-1) ** (len(pegs))) * pegs[-1]
    total = first + last
    if len(pegs) > 2:
        mid = construct_numerator_mid(pegs[1:-1])
        total += mid
    return 2 * total


def get_first_gear_fraction(pegs):
    if len(pegs) <= 1:
        return [-1, -1]

    denominator = 3 if len(pegs) % 2 == 0 else 1
    numerator = construct_numerator(pegs)

    # check if any radius went negative
    first_radius = Fraction(float(numerator)/denominator).limit_denominator()

    if first_radius < 2:
        return [-1, -1]

    current_radius = first_radius
    for i in range(0, len(pegs) -2):
        next_radius = (pegs[i + 1] - pegs[i]) - current_radius
        if next_radius < 1 or current_radius < 1:
            return [-1, -1]
        else:
            current_radius = next_radius

    return [first_radius.numerator, first_radius.denominator]


def solution(pegs):
    result = get_first_gear_fraction(pegs)
    print("{},{}".format(result[0], result[1]))
