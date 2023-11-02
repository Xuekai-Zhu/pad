def solution():
    theon_speed = 15
    yara_speed = 30
    distance = 90

    # Calculate the time it would take for Theon to reach the destination
    theon_time = distance / theon_speed

    # Calculate the time it would take for Yara to reach the destination
    yara_time = distance / yara_speed

    # Calculate the time difference
    time_diff = yara_time - theon_time
    result = time_diff
    return result

print(solution())