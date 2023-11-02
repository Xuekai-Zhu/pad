def solution():
    
    cattle_cost = 40000
    feeding_cost = 1.2 * cattle_cost
    total_cost = cattle_cost + feeding_cost
    total_weight = 100 * 1000
    price_per_pound = 2
    total_income = total_weight * price_per_pound
    profit = total_income - total_cost
    result = profit
    return result

print(solution())