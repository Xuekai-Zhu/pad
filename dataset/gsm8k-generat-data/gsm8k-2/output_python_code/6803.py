def solution():
    """The sum of the three sides of a triangle is 50. The right side of the triangle is 2 cm longer than the left side. Find the value of the triangle base if the left side has a value of 12 cm."""
    left_side = 12
    right_side = left_side + 2
    base = 50 - left_side - right_side
    result = base
    return result

print(solution())