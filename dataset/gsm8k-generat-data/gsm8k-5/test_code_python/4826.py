def solution():
    # Initialize variables
    three_points = 15
    two_points = 12
    total_points = 75

    # Calculate points scored for one point shots
    one_point = total_points - (3 * three_points) - (2 * two_points)

    # Return the number of times Tyson scored one point
    result = one_point
    return result

print(solution())