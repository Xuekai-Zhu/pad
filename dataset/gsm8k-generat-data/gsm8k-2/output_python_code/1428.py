def solution():
    """Ronald wants to make profits by re-selling some phones he bought a week ago. He bought 200 units for just $3000, and he wants to gain a third of the initial investment in profits when all units are sold. Including the profit margin, what will be the selling price for each phone?"""
    units = 200
    total_cost = 3000
    profit_margin = 1/3
    cost_per_unit = total_cost / units
    profit_per_unit = cost_per_unit * profit_margin
    selling_price = cost_per_unit + profit_per_unit
    result = selling_price
    return result

print(solution())