def solution():
    left_side = 12
    right_side = left_side + 2

    # Calculate the sum of the three sides of the triangle
    sum_of_sides = left_side + right_side + base

    # Solve for the value of the base using the sum of the sides equation
    base = sum_of_sides - (left_side + right_side)

    result = base
    return result

print(solution())