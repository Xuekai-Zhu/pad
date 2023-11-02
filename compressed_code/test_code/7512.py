def solution():
    
    unloaded_speed = 20
    loaded_speed = 10
    
    time_loaded_1 = 180 / loaded_speed
    time_unloaded_1 = 0
    time_loaded_2 = 80 / loaded_speed
    time_unloaded_2 = 0
    time_unloaded_3 = 120 / unloaded_speed
    time_loaded_3 = 0
    time_unloaded_4 = 140 / unloaded_speed

    total_time = time_loaded_1 + time_unloaded_1 + time_loaded_2 + time_unloaded_2 + time_unloaded_3 + time_loaded_3 + time_unloaded_4
    result = total_time
    
    return result

print(solution())