def solution():
    
    resisting_time = 20
    walking_distance = 64
    walking_speed = 8
    walking_time = walking_distance / walking_speed
    total_time = resisting_time + walking_time
    result = total_time
    return result

print(solution())