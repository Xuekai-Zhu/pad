def solution():
    small_ball_rubber_bands = 50  # Each small ball requires 50 rubber bands
    large_ball_rubber_bands = 300  # Each large ball requires 300 rubber bands
    initial_rubber_bands = 5000  # Michael brought a pack of 5,000 rubber bands
    small_balls_made = 22  # Michael already made 22 small balls

    # Calculate the total number of rubber bands used for small balls
    total_small_bands = small_balls_made * small_ball_rubber_bands

    # Calculate the remaining rubber bands
    remaining_bands = initial_rubber_bands - total_small_bands

    # Calculate the number of large balls Michael can make with the remaining rubber bands
    large_balls_made = remaining_bands // large_ball_rubber_bands
    result = large_balls_made
    return result

print(solution())