def solution():
    """Tim watches 2 shows. One of them is a half-hour show per episode and the other is a 1-hour long show per episode. The short show had 24 episodes and the long show had 12 episodes. How many hours of TV did he watch?"""
    # Calculate the total time for the half-hour show
    half_hour_time = 0.5 * 24

    # Calculate the total time for the one-hour show
    one_hour_time = 1 * 12

    # Calculate the total time watched in hours
    total_time = half_hour_time + one_hour_time

    # Return the result
    result = total_time
    return result

print(solution())