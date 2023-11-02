def solution():
    num_tires = 3
    tire_cost = 250
    window_cost = 700

    # Calculate the total cost of the tires
    total_tire_cost = num_tires * tire_cost

    # Calculate the total cost of all damages
    total_cost = total_tire_cost + window_cost
    result = total_cost
    return result

print(solution())