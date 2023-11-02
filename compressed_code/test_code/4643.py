def solution():
    
    speed_mph = 10
    time_1 = 0.5 
    distance_1 = speed_mph * time_1
    distance_2 = 15
    time_rest = 0.5 
    distance_3 = 20
    total_time = ((distance_1 + distance_2 + distance_3) / speed_mph) + time_rest
    result = total_time * 60 
    return result

print(solution())