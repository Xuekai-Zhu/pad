def solution():
    jerry_time = 30  # Time for round trip in minutes
    jerry_distance = 4  # Distance to school in miles
    carson_time = jerry_time / 2  # Time for one-way trip for Carson

    # Calculate Carson's speed in miles per hour
    carson_speed = jerry_distance / (carson_time / 60)

    result = carson_speed
    return result

print(solution())