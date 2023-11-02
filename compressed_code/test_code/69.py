def solution():
    
    starting_weight = 400
    increased_weight = starting_weight * 1.5
    price_per_pound = 3
    starting_value = starting_weight * price_per_pound
    increased_value = increased_weight * price_per_pound
    difference = increased_value - starting_value
    result = difference
    return result

print(solution())