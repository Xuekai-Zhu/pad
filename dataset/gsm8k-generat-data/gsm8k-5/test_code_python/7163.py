def solution():
    # Calculate time for first route
    uphill_time = 6
    path_time = 2 * uphill_time
    final_time = uphill_time / 3
    total_time_1 = uphill_time + path_time + final_time

    # Calculate time for second route
    flat_path_time = 14
    final_time_2 = 2 * flat_path_time
    total_time_2 = flat_path_time + final_time_2

    # Calculate the difference in time between the two routes
    diff = total_time_2 - total_time_1
    result = diff
    return result

print(solution())