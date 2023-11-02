def solution():
    
    distance_1 = 1500
    speed_1 = 75
    time_1 = distance_1 / speed_1
    
    distance_2 = 750
    speed_2 = 25
    time_2 = distance_2 / speed_2
    
    fastest_time = min(time_1, time_2)
    result = fastest_time
    
    return result

print(solution())