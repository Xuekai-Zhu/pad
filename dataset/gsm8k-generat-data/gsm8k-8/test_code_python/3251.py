def solution():
    # Define the number of rubber bands for each ball size
    small_ball_rubber_bands = 50
    large_ball_rubber_bands = 300

    # Define the number of rubber bands Michael has and has used so far
    total_rubber_bands = 5000
    used_rubber_bands = 22 * small_ball_rubber_bands

    # Calculate the number of rubber bands remaining
    remaining_rubber_bands = total_rubber_bands - used_rubber_bands

    # Calculate the number of large balls Michael can make with the remaining rubber bands
    number_of_large_balls = remaining_rubber_bands // large_ball_rubber_bands
    result = number_of_large_balls
    return result

print(solution())