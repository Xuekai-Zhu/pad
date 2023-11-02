def solution():
    # Calculate the time it would take to drive 1200 miles at 50 mph
    time_at_50mph = 1200 / 50

    # Calculate the time it would take to drive 1200 miles at 60 mph
    time_at_60mph = 1200 / 60

    # Calculate the difference in time between the two speeds
    time_saved = time_at_50mph - time_at_60mph

    result = time_saved
    return result

print(solution())