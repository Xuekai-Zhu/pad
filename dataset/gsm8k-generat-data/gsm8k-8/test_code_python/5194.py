def solution():
    # Calculate the cost to produce 100 patches
    cost_per_patch = 1.25
    total_cost = cost_per_patch * 100
    
    # Calculate the revenue from selling 100 patches
    sale_price_per_patch = 12.00
    total_revenue = sale_price_per_patch * 100
    
    # Calculate the net profit
    net_profit = total_revenue - total_cost
    result = net_profit
    return result

print(solution())