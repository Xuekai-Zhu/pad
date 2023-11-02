def solution():
    """The sum of the three sides of a triangle is 50. The right side of the triangle is 2 cm longer than the left side. Find the value of the triangle base if the left side has a value of 12 cm."""
    # Define the length of the left and right sides
    left_side = 12
    right_side = left_side + 2

    # Calculate the sum of the three sides
    sum_sides = left_side + right_side + base
    
    # Solve for the value of the base
    base = sum_sides - left_side - right_side

    # Display the value of the base
    result = base
    return result

print(solution())