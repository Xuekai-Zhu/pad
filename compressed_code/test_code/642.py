def solution():
    
    total_cost = 50 + 35 + 15
    desired_profit = 0.1 * total_cost
    total_profit = total_cost + desired_profit
    bags_of_corn = 10
    price_per_bag = total_profit / bags_of_corn
    result = price_per_bag
    return result

print(solution())