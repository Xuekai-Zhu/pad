def solution():
    patches_per_unit = 100  # Sean orders patches in units of 100
    cost_per_patch = 1.25  # Sean pays $1.25 per patch
    selling_price_per_unit = 1200  # Sean sells 100 patches for $12.00 each

    # Calculate the cost of one unit of patches
    cost_per_unit = patches_per_unit * cost_per_patch

    # Calculate the revenue from selling one unit of patches
    revenue_per_unit = selling_price_per_unit * patches_per_unit

    # Calculate the net profit from selling one unit of patches
    net_profit_per_unit = revenue_per_unit - cost_per_unit

    result = net_profit_per_unit
    return result

print(solution())