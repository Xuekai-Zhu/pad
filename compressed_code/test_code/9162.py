def solution():
    
    pond_capacity = 200
    normal_pump_rate = 6  
    drought_pump_rate = 2/3 * normal_pump_rate
    time_to_fill = pond_capacity / drought_pump_rate
    result = time_to_fill
    return result

print(solution())