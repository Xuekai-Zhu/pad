def solution():
    total_distance = 120  # miles
    initial_speed = 60  # miles per hour
    initial_time = 0.5  # hours (30 minutes)
    remaining_time = 1.5 - initial_time  # hours (1 hour 30 minutes - 30 minutes)
    remaining_distance = total_distance - initial_speed * initial_time

    # Calculate the required average speed for the remaining distance
    required_average_speed = remaining_distance / remaining_time
    result = required_average_speed
    return result

print(solution())