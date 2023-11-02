def solution():
    time_per_8_times = 20  # minutes
    num_times = 6

    # Calculate the time it takes for John to go to the bathroom 1 time
    time_per_1_time = time_per_8_times / 8

    # Calculate the total time it would take for John to go to the bathroom 6 times
    total_time = time_per_1_time * num_times
    result = total_time
    return result

print(solution())