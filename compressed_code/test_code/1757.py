def solution():
    
    starting_amount = 20
    peaches_cost_per_pound = 2
    pounds_of_peaches_bought = 3
    total_cost_of_peaches = peaches_cost_per_pound * pounds_of_peaches_bought
    amount_left = starting_amount - total_cost_of_peaches
    result = amount_left
    return result

print(solution())