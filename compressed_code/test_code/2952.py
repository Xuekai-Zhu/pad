def solution():
    
    distance = 60
    time = 1
    overspeed = 10
    average_speed = distance / time
    speed_limit = average_speed - overspeed
    result = speed_limit
    return result

print(solution())