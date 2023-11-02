def solution():
    pond_capacity = 200
    normal_pump_speed = 6
    reduced_pump_speed = normal_pump_speed * (2/3)
    minutes_to_fill_pond = pond_capacity / reduced_pump_speed
    result = minutes_to_fill_pond
    return result

print(solution())