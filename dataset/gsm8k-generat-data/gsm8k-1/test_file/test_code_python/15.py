def solution():
    """Marissa is hiking a 12-mile trail. She took 1 hour to walk the first 4 miles,
    then another hour to walk the next two miles.
    If she wants her average speed to be 4 miles per hour,
    what speed (in miles per hour) does she need to walk the remaining distance?"""
    total_distance = 12
    distance_covered = 4 + 2
    remaining_distance = total_distance - distance_covered
    time_taken = 2  # in hours
    desired_average_speed = 4  # in mph
    speed_needed = (remaining_distance / (desired_average_speed * 1.0)) - time_taken
    result = speed_needed
    return result

print(solution())