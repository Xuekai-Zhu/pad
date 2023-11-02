def solution():
    
    
    flat_distance = 20 * 4.5
    uphill_distance = 12 * 2.5
    downhill_distance = 24 * 1.5

    
    total_bike_distance = flat_distance + uphill_distance + downhill_distance

    
    walking_distance = 164 - total_bike_distance

    result = walking_distance
    return result

print(solution())