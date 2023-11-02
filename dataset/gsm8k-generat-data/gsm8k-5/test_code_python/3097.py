def solution():
    distance = 90  # The destination is 90 nautical miles away
    theon_speed = 15  # Theon's ship can move 15 nautical miles per hour
    yara_speed = 30  # Yara's ship can move 30 nautical miles per hour

    # Calculate the time taken by each ship to reach the destination
    theon_time = distance / theon_speed
    yara_time = distance / yara_speed

    # Calculate the time difference between the two ships
    time_difference = yara_time - theon_time
    result = time_difference
    return result

print(solution())