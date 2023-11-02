def solution():
    small_ball_rubber_bands = 50
    large_ball_rubber_bands = 300
    total_rubber_bands = 5000
    small_balls_made = 22

    # Calculate the total rubber bands used by the small balls
    small_balls_rubber_bands_used = small_balls_made * small_ball_rubber_bands

    # Calculate the remaining rubber bands
    remaining_rubber_bands = total_rubber_bands - small_balls_rubber_bands_used

    # Calculate the number of large balls that can be made with the remaining rubber bands
    num_large_balls = remaining_rubber_bands // large_ball_rubber_bands
    result = num_large_balls
    return result

print(solution())