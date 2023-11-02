def solution():
    
    tank_capacity = 200
    empty_weight = 80
    filled_capacity = tank_capacity * 0.8
    filled_weight = filled_capacity * 8
    total_weight = empty_weight + filled_weight
    result = total_weight
    return result

print(solution())