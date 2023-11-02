def solution():
    smallest_angle = x
    largest_angle = 5 * x
    middle_angle = 3 * x
    total_angles = smallest_angle + middle_angle + largest_angle

    # Use the fact that the sum of angles in a triangle is 180 degrees to solve for x
    # smallest_angle + middle_angle + largest_angle = 180
    # substitute in the expressions for the angles
    # x + 3x + 5x = 180
    # simplify
    # 9x = 180
    # x = 20

    smallest_angle = 20
    result = smallest_angle
    return result

print(solution())