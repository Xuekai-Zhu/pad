def solution():
    
    joseph_speed = 50
    kyle_speed = 62
    joseph_time = 2.5
    kyle_time = 2
    joseph_distance = joseph_speed * joseph_time
    kyle_distance = kyle_speed * kyle_time
    more_distance = joseph_distance - kyle_distance
    result = more_distance
    return result

print(solution())