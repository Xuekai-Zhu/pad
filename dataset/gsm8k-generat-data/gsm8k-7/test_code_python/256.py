def solution():
    map_scale = 1/4
    actual_distance_per_inch = 8

    # Calculate the actual distance represented by 3 3/8 inches
    total_actual_distance = (3 + (3/8)) * actual_distance_per_inch

    # Calculate the actual distance in miles
    actual_distance = total_actual_distance * map_scale
    result = actual_distance
    return result

print(solution())