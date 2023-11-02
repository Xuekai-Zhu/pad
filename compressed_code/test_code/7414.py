def solution():
    
    length = 100
    width = 50
    laps = 6
    distance_per_lap = (2 * length) + (2 * width)
    total_distance = laps * distance_per_lap
    result = total_distance
    return result

print(solution())