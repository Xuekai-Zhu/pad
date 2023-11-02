def solution():
    
    total_liters = 1000 * 10
    tank_capacity = 500
    num_tanks = total_liters // tank_capacity
    if total_liters % tank_capacity != 0:
        num_tanks += 1
    result = num_tanks
    return result

print(solution())