def solution():
    
    second_tank_capacity = 450 / 0.45
    total_capacity = 2 * second_tank_capacity
    water_needed = total_capacity - 300 - 450
    result = water_needed
    return result

print(solution())