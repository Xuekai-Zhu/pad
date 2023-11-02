def solution():
    
    distance = 1200
    speed_1 = 50
    speed_2 = 60
    time_1 = distance / speed_1
    time_2 = distance / speed_2
    time_saved = time_1 - time_2
    result = time_saved
    return result

print(solution())