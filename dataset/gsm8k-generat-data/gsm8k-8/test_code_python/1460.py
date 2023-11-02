def solution():
    # Calculate the distance covered in the first 4 hours
    distance_covered = 4 * 4

    # Calculate the distance remaining
    distance_remaining = 24 - distance_covered

    # Calculate the time remaining
    time_remaining = 8 - 4

    # Calculate the speed needed to cover the remaining distance in the remaining time
    speed_needed = distance_remaining / time_remaining
    result = speed_needed
    return result

print(solution())