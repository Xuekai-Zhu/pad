def solution():
    total_distance = 12  # Marissa is hiking a 12-mile trail
    time_1 = 1  # Marissa took 1 hour to walk the first 4 miles
    time_2 = 2  # Marissa took 2 hour to walk the next two miles
    average_speed = 4  # Marissa wants her average speed to be 4 miles per hour

    # Calculate the distance Marissa needs to walk
    distance_to_walk = total_distance - time_1 - time_2

    # Calculate the speed Marissa needs to walk the remaining distance
    remaining_distance = total_distance - distance_to_walk
    speed_needed = remaining_distance / average_speed
    result = speed_needed
    return result

print(solution())