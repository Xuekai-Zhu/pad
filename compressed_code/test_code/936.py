def solution():
    
    distance = 448
    time_first = 0.5  
    time_second = 1  
    speed_first = distance / time_first
    speed_second = distance / time_second
    speed_difference = abs(speed_first - speed_second)
    result = speed_difference
    return result

print(solution())