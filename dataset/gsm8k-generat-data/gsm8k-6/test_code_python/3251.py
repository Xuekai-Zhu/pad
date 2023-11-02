def solution():
    # Calculate the number of rubber bands used for the small balls
    small_balls_rubber_bands = 22 * 50

    # Calculate the remaining rubber bands
    remaining_rubber_bands = 5000 - small_balls_rubber_bands

    # Calculate the number of large balls that can be made with the remaining rubber bands
    large_balls = remaining_rubber_bands // 300

    result = large_balls
    return result

print(solution())