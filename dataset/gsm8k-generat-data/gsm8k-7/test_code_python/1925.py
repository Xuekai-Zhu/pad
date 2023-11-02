def solution():
    lake_dist = 1.5  # half of the total race distance (3 miles)
    ocean_dist = 1.5  # half of the total race distance (3 miles)
    lake_speed = 3  # in miles per hour
    ocean_speed = 2.5  # in miles per hour

    # Calculate the time it takes to swim in the lake
    time_in_lake = lake_dist / lake_speed

    # Calculate the time it takes to swim in the ocean
    time_in_ocean = ocean_dist / ocean_speed

    # Calculate the total time spent in races
    total_time = 10 * (time_in_lake + time_in_ocean)
    result = total_time
    return result

print(solution())