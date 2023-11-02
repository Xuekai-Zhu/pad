def solution():
    
    
    cubic_feet = 6
    gallons = cubic_feet * 7.5
    pounds_of_water = gallons * 8

    
    tablespoons_per_pound = 1.5
    tablespoons_needed = pounds_of_water * tablespoons_per_pound
    cost_per_tablespoon = 0.5
    total_cost = tablespoons_needed * cost_per_tablespoon

    result = total_cost
    return result

print(solution())