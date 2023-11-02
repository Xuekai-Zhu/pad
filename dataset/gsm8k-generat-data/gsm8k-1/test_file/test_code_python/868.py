def solution():
    """Seven bottles of soda cost $21.00 while 4 bottles of water cost $8. If David wants to buy 3 bottles of soda and 2 bottles of water, how much will that cost?"""
    soda_cost_per_bottle = 3
    water_cost_per_bottle = 2
    soda_total_cost = soda_cost_per_bottle * 3
    water_total_cost = water_cost_per_bottle * 2
    total_cost = soda_total_cost + water_total_cost
    result = total_cost
    return result

print(solution())