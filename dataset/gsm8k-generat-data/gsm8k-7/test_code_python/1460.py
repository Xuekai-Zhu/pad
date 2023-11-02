def solution():
    total_distance = 24
    total_time = 8
    initial_speed = 4
    initial_time = 4

    # Calculate the distance covered in the first 4 hours
    initial_distance = initial_speed * initial_time

    # Calculate the remaining distance
    remaining_distance = total_distance - initial_distance

    # Calculate the remaining time
    remaining_time = total_time - initial_time

    # Calculate the required speed for the remaining journey to be completed on time
    required_speed = remaining_distance / remaining_time
    result = required_speed
    return result

print(solution())