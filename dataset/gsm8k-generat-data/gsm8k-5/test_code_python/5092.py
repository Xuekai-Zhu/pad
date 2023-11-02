def solution():
    # Calculate the original travel time
    original_time = 600 / 50  # 600 miles at 50 mph

    # Calculate the new travel time
    new_time = original_time - 4  # Decrease travel time by 4 hours

    # Calculate the required speed for the new travel time
    required_speed = 600 / new_time

    # Calculate the increase in speed required
    increase_speed = required_speed - 50

    result = increase_speed
    return result

print(solution())