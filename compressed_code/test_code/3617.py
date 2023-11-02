def solution():
    
    cost_per_liter = 1.4
    friday_price = cost_per_liter - 0.4
    first_purchase = 10 * cost_per_liter
    second_purchase = 25 * friday_price
    total_cost = first_purchase + second_purchase
    result = total_cost
    return result

print(solution())