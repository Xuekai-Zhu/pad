def solution():
    """Sean designs and sells patches. He orders his patches in a unit of 100 and is charged $1.25 per patch. If he turns around and sells all 100 patches for $12.00 each, what is his net profit?"""
    cost_per_patch = 1.25
    sale_price_per_unit = 1200
    patches_per_unit = 100
    revenue_per_unit = sale_price_per_unit * patches_per_unit
    cost_per_unit = cost_per_patch * patches_per_unit
    net_profit = revenue_per_unit - cost_per_unit
    result = net_profit
    return result

print(solution())