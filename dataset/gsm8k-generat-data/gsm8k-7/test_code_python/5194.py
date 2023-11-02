def solution():
    num_patches = 100
    cost_per_patch = 1.25
    selling_price_per_patch = 12.0

    # Calculate the total cost of ordering 100 patches
    total_cost = num_patches * cost_per_patch

    # Calculate the total revenue from selling 100 patches
    total_revenue = num_patches * selling_price_per_patch

    # Calculate the net profit
    net_profit = total_revenue - total_cost
    result = net_profit
    return result

print(solution())