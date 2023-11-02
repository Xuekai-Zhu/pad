def solution():
    cost_of_seeds = 50
    cost_of_fertilizer = 35
    cost_of_labor = 15
    total_cost = cost_of_seeds + cost_of_fertilizer + cost_of_labor
    desired_profit = 10
    bags_of_corn = 10
    cost_per_bag = total_cost / bags_of_corn
    selling_price_per_bag = cost_per_bag * (1 + (desired_profit/100))
    result = selling_price_per_bag
    
    return result

print(solution())