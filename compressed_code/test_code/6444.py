def solution():
    
    total_cost = 50 + 35 + 15
    bags = 10
    cost_per_bag = total_cost / bags
    profit_percent = 10
    selling_price_per_bag = cost_per_bag * (1 + (profit_percent / 100))
    result = selling_price_per_bag
    return result

print(solution())