def solution():
    flat_sand_speed = 60
    downhill_speed = flat_sand_speed + 12
    uphill_speed = flat_sand_speed - 18

    time_on_flat = 1/3
    time_on_downhill = 1/3
    time_on_uphill = 1/3

    # Calculate the total distance traveled
    total_distance = 1

    # Calculate the distance traveled on each slope
    distance_on_flat = time_on_flat * total_distance
    distance_on_downhill = time_on_downhill * total_distance
    distance_on_uphill = time_on_uphill * total_distance

    # Calculate the total time for the whole trip
    total_time = (distance_on_flat / flat_sand_speed) + (
        distance_on_downhill / downhill_speed) + (distance_on_uphill / uphill_speed)

    # Calculate the average speed
    average_speed = total_distance / total_time
    result = average_speed
    return result

print(solution())