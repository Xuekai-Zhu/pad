def solution():
    # Calculate the total distance Tyson swam
    total_distance = 10 * 3

    # Calculate the distance swam in lakes and oceans
    lake_distance = total_distance / 2
    ocean_distance = total_distance / 2

    # Calculate the time spent swimming in lakes and oceans
    time_in_lakes = lake_distance / 3
    time_in_oceans = ocean_distance / 2.5

    # Calculate the total time spent swimming
    total_time = time_in_lakes + time_in_oceans
    result = total_time
    return result

print(solution())