def solution():
    
    pond_capacity = 200
    normal_pump_speed = 6
    reduced_pump_speed = (2/3) * normal_pump_speed
    time_to_fill_pond = pond_capacity / reduced_pump_speed
    result = time_to_fill_pond
    return result

print(solution())