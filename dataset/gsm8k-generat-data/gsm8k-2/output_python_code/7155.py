def solution():
    """Rich ran a 24-mile marathon in 3 hours and 36 minutes. On average, how long, in minutes, did it take Rich to run a mile during the race?"""
    total_time = 3 * 60 + 36  # convert hours to minutes
    distance = 24
    time_per_mile = total_time / distance
    result = time_per_mile
    return result

print(solution())