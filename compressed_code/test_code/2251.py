def solution():
    
    distance = 150
    time = 2
    speed_limit = 60
    actual_speed = distance / time
    above_speed_limit = actual_speed - speed_limit
    result = above_speed_limit
    return result

print(solution())