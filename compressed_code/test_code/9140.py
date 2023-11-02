def solution():
    
    distance = 12
    speed_to = 4
    speed_back = 6
    time_to = distance / speed_to
    time_back = distance / speed_back
    total_time = time_to + time_back
    result = total_time
    return result

print(solution())