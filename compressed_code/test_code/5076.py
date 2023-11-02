def solution():
    
    initial_temp = 60
    heat_rate = 5
    target_temp_1 = 240
    cool_rate = 7
    target_temp_2 = 170

    
    time_to_heat = (target_temp_1 - initial_temp) / heat_rate

    
    time_to_cool = (target_temp_1 - target_temp_2) / cool_rate

    
    total_time = time_to_heat + time_to_cool

    result = total_time
    return result

print(solution())