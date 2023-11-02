def solution():
    total_air_time = 1.5
    num_commercials = 3
    commercial_duration = 0.1667  # 10 minutes in hours

    # Calculate the total duration of commercials
    total_commercial_duration = num_commercials * commercial_duration

    # Calculate the duration of the TV show itself
    tv_show_duration = total_air_time - total_commercial_duration
    result = tv_show_duration
    return result

print(solution())