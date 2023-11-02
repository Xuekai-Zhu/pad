def solution():
    # Calculate the time it takes for Theon's ship to reach the destination
    theon_time = 90 / 15  # distance / speed = time

    # Calculate the time it takes for Yara's ship to reach the destination
    yara_time = 90 / 30

    # Calculate the time difference between Yara and Theon
    time_difference = yara_time - theon_time
    result = time_difference
    return result

print(solution())