def solution():
    distance_1 = 5
    rate_1 = 10  # minutes per mile

    distance_2 = 4
    rate_2 = 9.5  # minutes per mile

    # Calculate the time it takes Rudy to run the first distance
    time_1 = distance_1 * rate_1

    # Calculate the time it takes Rudy to run the second distance
    time_2 = distance_2 * rate_2

    # Calculate the total time Rudy runs
    total_time = time_1 + time_2
    result = total_time
    return result

print(solution())