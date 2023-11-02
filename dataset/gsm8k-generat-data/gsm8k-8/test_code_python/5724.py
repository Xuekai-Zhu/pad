def solution():
    total_distance = 120  # miles
    first_half_distance = 60  # miles
    first_half_time = 0.5  # hours
    second_half_distance = total_distance - first_half_distance
    second_half_time = 1.5 - first_half_time  # hours

    # Calculate the required speed for the second half
    required_speed = second_half_distance / second_half_time

    result = required_speed
    return result

print(solution())