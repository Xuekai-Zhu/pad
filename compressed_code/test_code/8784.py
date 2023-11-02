def solution():
    
    distance = 60
    time = 1
    speed_over_limit = 10
    actual_speed = distance / time
    speed_limit = actual_speed - speed_over_limit
    result = speed_limit
    return result

print(solution())