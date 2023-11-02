def solution():
    # Calculate Jerome's speed in MPH
    jerome_speed = 4  # MPH
    jerome_time = 6  # hours
    jerome_distance = jerome_speed * jerome_time  # miles

    # Calculate Nero's speed in MPH
    nero_time = 3  # hours
    nero_distance = jerome_distance  # assume both ran the same distance
    nero_speed = nero_distance / nero_time  # MPH

    result = nero_speed
    return result

print(solution())