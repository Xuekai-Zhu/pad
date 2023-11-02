def solution():
    
    tank_capacity = 200
    empty_tank_weight = 80
    filled_tank_volume = 0.8 * tank_capacity
    filled_tank_weight = (filled_tank_volume * 8) + empty_tank_weight
    result = filled_tank_weight
    return result

print(solution())