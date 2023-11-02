def solution():
    # Define the distances
    distance_slc_lv = 420
    distance_lv_la = 273

    # Define the total time and subtract time for rest stops
    total_time = 11
    rest_stops = 1
    available_time = total_time - rest_stops

    # Calculate the minimum average speed
    minimum_speed = (distance_slc_lv + distance_lv_la) / available_time
    result = minimum_speed
    return result

print(solution())