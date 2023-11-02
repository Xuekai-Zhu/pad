def solution():
    # Calculate the time it would take each person to run the 24 mile race
    apple_time = 24 / 3  # hours
    mac_time = 24 / 4  # hours

    # Calculate the time difference between their races in minutes
    time_difference = (mac_time - apple_time) * 60  # minutes
    result = time_difference
    return result

print(solution())