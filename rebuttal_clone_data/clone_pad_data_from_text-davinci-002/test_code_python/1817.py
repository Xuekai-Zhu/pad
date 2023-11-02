def solution():
    total_tires = 4
    flat_tires = 2
    tire_capacity = 500
    amount_to_pump = 50
    pumps_needed = (total_tires - flat_tires) * (tire_capacity / amount_to_pump)
    result = pumps_needed
    
    return result

print(solution())