def solution():
    
    starting_weight = 400
    weight_increase = 1.5
    current_weight = starting_weight * weight_increase
    price_per_pound = 3
    initial_worth = starting_weight * price_per_pound
    new_worth = current_weight * price_per_pound
    profit = new_worth - initial_worth
    result = profit
    return result

print(solution())