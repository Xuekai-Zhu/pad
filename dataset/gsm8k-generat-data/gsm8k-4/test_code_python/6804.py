def solution():
    """The sum of the three sides of a triangle is 50. The right side of the triangle is 2 cm longer than the left side.
    Find the value of the triangle base if the left side has a value of 12 cm."""
    # Define the left side and the right side of the triangle
    left_side = 12
    right_side = left_side + 2

    # Calculate the sum of the three sides
    sum_sides = left_side + right_side + base

    # Calculate the value of the base
    base = sum_sides - left_side - right_side

    result = base
    return result

print(solution())