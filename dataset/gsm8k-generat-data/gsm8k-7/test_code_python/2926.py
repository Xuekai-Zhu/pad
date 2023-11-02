def solution():
    apple_speed = 3  # miles per hour
    mac_speed = 4  # miles per hour
    distance = 24  # miles

    # Calculate the time Apple takes to finish the race
    apple_time = distance / apple_speed  # hours
    apple_time_minutes = apple_time * 60  # minutes

    # Calculate the time Mac takes to finish the race
    mac_time = distance / mac_speed  # hours
    mac_time_minutes = mac_time * 60  # minutes

    # Calculate how much faster Mac is compared to Apple
    time_difference = apple_time_minutes - mac_time_minutes
    result = time_difference
    return result

print(solution())