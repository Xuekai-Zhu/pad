def solution():
    # First route
    uphill_time = 6
    path_time = 2 * uphill_time
    downhill_time = (uphill_time + path_time) / 3
    first_route_time = uphill_time + path_time + downhill_time

    # Second route
    flat_path_time = 14
    second_half_time = 2 * flat_path_time
    second_route_time = flat_path_time + second_half_time

    # Calculate the difference in time between the two routes
    time_difference = second_route_time - first_route_time
    result = time_difference
    return result

print(solution())