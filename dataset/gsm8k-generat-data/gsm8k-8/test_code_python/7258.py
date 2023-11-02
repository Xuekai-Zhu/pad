def solution():
    # Define the point values
    single_points = 1000
    tetris_points = 8 * single_points

    # Calculate the total point value of Tim's score
    total_points = (6 * single_points) + (4 * tetris_points)

    result = total_points
    return result

print(solution())