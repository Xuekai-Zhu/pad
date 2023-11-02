def solution():
    # Calculate the distance covered in the first 4 hours
    distance_covered = 4 * 4  # distance = speed * time 

    # Calculate the remaining distance
    remaining_distance = 24 - distance_covered

    # Calculate the required speed for the remaining distance to be covered in the remaining time
    required_speed = remaining_distance / 4  # time remaining = 8 - 4 = 4 hours

    result = required_speed
    return result

print(solution())