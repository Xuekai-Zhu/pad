def solution():
    
    
    
    total_distance = 210
    friend_distance = 40 * 3
    christina_distance = total_distance - friend_distance
    
    
    christina_speed = 30
    christina_time = christina_distance / christina_speed
    minutes_driving = christina_time * 60
    
    result = minutes_driving
    return result

print(solution())