def solution():
    
    total_distance = 210
    christina_speed = 30
    friend_speed = 40
    friend_time = 3
    friend_distance = friend_speed * friend_time
    christina_distance = total_distance - friend_distance
    christina_time = christina_distance / christina_speed
    christina_time_in_minutes = christina_time * 60
    result = christina_time_in_minutes
    return result

print(solution())