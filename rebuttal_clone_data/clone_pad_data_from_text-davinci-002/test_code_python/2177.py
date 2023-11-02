def solution():
    unloaded_speed = 20
    loaded_speed = 10
    unloaded_distance = 180
    loaded_distance = 120 + 80 + 140
    unloaded_time = unloaded_distance / unloaded_speed
    loaded_time = loaded_distance / loaded_speed
    total_time = unloaded_time + loaded_time
    result = total_time
    
    return result

print(solution())