def solution():
    total_distance = 24  # Rich ran a 24-mile marathon
    total_time_in_minutes = (3 * 60) + 36  # Rich took 3 hours and 36 minutes to complete the marathon

    # Calculate the average time, in minutes, that it took for Rich to run a mile
    average_time_per_mile = total_time_in_minutes / total_distance
    result = average_time_per_mile
    return result

print(solution())