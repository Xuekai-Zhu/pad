def solution():
    
    bags_to_sell = 100
    selling_price_per_bag = 10
    desired_profit = 300
    cost_per_bag = (bags_to_sell * selling_price_per_bag - desired_profit) / bags_to_sell
    result = cost_per_bag
    return result

print(solution())