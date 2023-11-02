def solution():
    
    distance_north = 55
    distance_west = 95
    speed = 25
    time_north = distance_north / speed
    time_west = distance_west / speed
    total_time = time_north + time_west
    result = total_time
    return result

print(solution())