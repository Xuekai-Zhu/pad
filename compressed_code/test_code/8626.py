def solution():
    
    distance = 200
    speed_24 = 50
    speed_12 = 20
    time_24 = distance / speed_24
    time_12 = distance / speed_12
    time_difference = time_12 - time_24
    result = time_difference
    return result

print(solution())