def solution():
    
    gas_mileage = 35
    tank_size = 12
    total_distance = 372
    actual_mileage = total_distance / tank_size
    difference = gas_mileage - actual_mileage
    result = difference
    return result

print(solution())