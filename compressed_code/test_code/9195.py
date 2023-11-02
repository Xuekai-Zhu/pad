def solution():
    
    distance = 1200
    speed1 = 50
    speed2 = 60
    time1 = distance / speed1
    time2 = distance / speed2
    time_saved = time1 - time2
    result = time_saved
    return result

print(solution())