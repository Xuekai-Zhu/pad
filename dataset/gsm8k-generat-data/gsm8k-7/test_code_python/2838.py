def solution():
    lionel_distance = 4
    esther_distance = 975 / 1760  # convert yards to miles
    niklaus_distance = 1287 / 5280  # convert feet to miles

    # Calculate total distance in miles
    total_distance = lionel_distance + esther_distance + niklaus_distance

    # Convert total distance to feet
    total_distance_feet = total_distance * 5280
    result = total_distance_feet
    return result

print(solution())