def solution():
    
    distance_1 = 200
    speed_1 = 50
    time_1 = distance_1 / speed_1
    distance_2 = 240
    speed_2 = 80
    time_2 = distance_2 / speed_2
    average_time = (time_1 + time_2) / 2
    result = round(average_time)
    return result

print(solution())