def solution():
    left_side = 12  # Given that the left side has a value of 12 cm
    right_side = left_side + 2  # Given that the right side is 2 cm longer than the left side
    sum_sides = 50  # Given that the sum of the three sides is 50 cm

    # Calculate the value of the base of the triangle
    base = sum_sides - left_side - right_side
    result = base
    return result

print(solution())