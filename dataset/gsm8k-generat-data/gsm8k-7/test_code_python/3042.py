def solution():
    distance_slc_lv = 420
    distance_lv_la = 273
    total_distance = distance_slc_lv + distance_lv_la
    total_time = 11  # hours

    # Calculate the average speed in miles per hour
    avg_speed = total_distance / total_time
    result = avg_speed
    return result

print(solution())