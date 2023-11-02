def solution():
    beef_pounds = 4
    veggies_pounds = 6
    price_beef_per_pound = 3 * 2
    price_veggies_per_pound = 2
    cost_beef = beef_pounds * price_beef_per_pound
    cost_veggies = veggies_pounds * price_veggies_per_pound
    total_cost = cost_beef + cost_veggies
    result = total_cost
    
    return result

print(solution())