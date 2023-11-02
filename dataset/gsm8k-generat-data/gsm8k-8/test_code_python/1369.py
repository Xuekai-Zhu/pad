def solution():
    # Define total points and ratios
    total_points = 810
    first_to_second_ratio = 1/3
    second_to_third_ratio = 3

    # Calculate second bowler's points
    second_points = (total_points / (1 + 1/3 + 3))

    # Calculate third bowler's points using ratios
    third_points = second_points / 3
    first_points = second_points / 3

    # Return third bowler's points
    result = third_points
    return result

print(solution())