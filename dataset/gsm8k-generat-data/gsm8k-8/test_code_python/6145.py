def solution():
    # Calculate the time it takes to fill one barrel with the leak
    leak_time = 5

    # Calculate the time it takes to fill one barrel without the leak
    normal_time = 3

    # Calculate the difference in time to fill one barrel with and without the leak
    time_difference = leak_time - normal_time

    # Calculate the time it takes to fill 12 barrels with the leak
    leak_time_to_fill_12 = 12 * leak_time

    # Calculate the time it takes to fill 12 barrels without the leak
    normal_time_to_fill_12 = 12 * normal_time

    # Calculate the difference in time to fill 12 barrels with and without the leak
    time_difference_to_fill_12 = leak_time_to_fill_12 - normal_time_to_fill_12

    result = time_difference_to_fill_12
    return result

print(solution())