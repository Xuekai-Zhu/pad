def solution():
    distance_to_idaho = 640  # Distance from Washington to Idaho
    distance_to_nevada = 550  # Distance from Idaho to Nevada
    speed_to_idaho = 80  # Speed from Washington to Idaho in miles per hour
    speed_to_nevada = 50  # Speed from Idaho to Nevada in miles per hour

    # Calculate the time it takes to travel from Washington to Idaho
    time_to_idaho = distance_to_idaho / speed_to_idaho

    # Calculate the time it takes to travel from Idaho to Nevada
    time_to_nevada = distance_to_nevada / speed_to_nevada

    # Calculate total time it takes to arrive at the destination
    total_time = time_to_idaho + time_to_nevada
    result = total_time
    return result

print(solution())