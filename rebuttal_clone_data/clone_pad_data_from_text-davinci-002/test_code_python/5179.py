def solution():
    tank_capacity = 200
    empty_tank_weight = 80
    full_tank_percent = 80
    full_tank_amount = tank_capacity * (full_tank_percent / 100)
    weight_per_gallon = 8
    full_tank_weight = full_tank_amount * weight_per_gallon
    result = full_tank_weight
    return result

print(solution())