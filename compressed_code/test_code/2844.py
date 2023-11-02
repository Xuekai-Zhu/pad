def solution():
    
    distance = 10
    speed1 = 3
    time1 = 2
    speed2 = 1
    time2 = (distance - (speed1 * time1)) / speed2
    total_time = time1 + time2
    result = total_time
    return result

print(solution())