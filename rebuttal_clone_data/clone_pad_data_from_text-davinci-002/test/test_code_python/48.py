def solution():
    
    initial_weight = 400
    increase_factor = 1.5
    increased_weight = initial_weight * increase_factor
    price_per_pound = 3
    increased_value = increased_weight * price_per_pound
    result = increased_value - (initial_weight * price_per_pound)
    return result

print(solution())