def solution():
    # Calculate the time taken for the first route
    time_uphill = 6
    time_path = 2 * time_uphill
    time_finish = time_path / 3
    time_route1 = time_uphill + time_path + time_finish

    # Calculate the time taken for the second route
    time_flat = 14
    time_finish2 = 2 * time_flat
    time_route2 = time_flat + time_finish2

    # Calculate the difference in time between the two routes
    difference = time_route2 - time_route1
    result = difference
    return result

print(solution())