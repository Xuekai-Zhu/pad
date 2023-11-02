def solution():
    left_side = 12  # given left side value
    right_side = left_side + 2  # right side is 2 cm longer than left side
    base = 50 - (left_side + right_side)  # calculate the base using the sum of the three sides
    result = base
    return result

print(solution())