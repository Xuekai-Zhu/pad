def solution():
    # Calculate the total time Martin spent traveling
    total_time = 8

    # Calculate the time spent traveling at each speed
    time_at_70kmh = total_time / 2
    time_at_85kmh = total_time / 2

    # Calculate the distance traveled at each speed
    distance_at_70kmh = time_at_70kmh * 70
    distance_at_85kmh = time_at_85kmh * 85

    # Calculate the total distance traveled
    total_distance = distance_at_70kmh + distance_at_85kmh
    result = total_distance
    return result

print(solution())