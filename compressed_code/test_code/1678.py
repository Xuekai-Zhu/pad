def solution():
    
    total_profit = 300
    selling_price = 10
    total_selling_price = selling_price * 100
    total_cost = total_selling_price - total_profit
    cost_per_bag = total_cost / 100
    result = cost_per_bag
    return result

print(solution())