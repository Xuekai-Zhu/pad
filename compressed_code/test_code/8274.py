def solution():
    
    initial_tank_capacity = 4000
    transfer_amount = initial_tank_capacity * 0.75
    initial_large_tank = 3000
    large_tank_capacity = 20000
    large_tank_level = initial_large_tank + transfer_amount
    half_tank_capacity = large_tank_capacity / 2
    liters_needed = half_tank_capacity - large_tank_level
    result = liters_needed
    return result

print(solution())