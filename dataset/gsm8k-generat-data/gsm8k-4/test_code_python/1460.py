def solution():
    """A man intends to complete a journey of 24 km in 8 hours. If he travels at a speed of 4km/hr for the first four hours, at what speed does he need to travel for the remainder of the journey to be right on time?"""
    # Define the total distance to be covered and the time available
    total_distance = 24
    total_time = 8

    # Define the distance covered in the first four hours and the time remaining
    distance_covered = 4 * 4
    time_remaining = total_time - 4

    # Calculate the remaining distance
    remaining_distance = total_distance - distance_covered

    # Calculate the speed needed to cover the remaining distance in the remaining time
    speed_needed = remaining_distance / time_remaining

    # return the result
    result = speed_needed
    return result

print(solution())