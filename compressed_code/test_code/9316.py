def solution():
    
    total_cost = 224
    tire_cost = 42
    num_tires = 4
    tire_total_cost = tire_cost * num_tires
    battery_cost = total_cost - tire_total_cost
    result = battery_cost
    return result

print(solution())