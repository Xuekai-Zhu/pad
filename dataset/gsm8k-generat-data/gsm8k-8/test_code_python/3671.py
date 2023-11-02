def solution():
    # Calculate the distance Diana can bike at 3 mph for 2 hours
    distance_at_3mph = 3 * 2

    # Calculate the distance remaining after biking at 3 mph
    remaining_distance = 10 - distance_at_3mph

    # Calculate the time it takes to bike the remaining distance at 1 mph
    time_at_1mph = remaining_distance / 1

    # Calculate the total time it takes to get home
    total_time = time_at_1mph + 2

    result = total_time
    return result

print(solution())