def solution():
    
    cost_per_patch = 1.25
    selling_price_per_patch = 12.00
    num_patches = 100
    total_cost = cost_per_patch * num_patches
    total_revenue = selling_price_per_patch * num_patches
    net_profit = total_revenue - total_cost
    result = net_profit
    return result

print(solution())