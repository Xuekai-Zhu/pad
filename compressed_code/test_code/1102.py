def solution():
    
    units = 200
    total_cost = 3000
    profit_margin = 1/3
    cost_per_unit = total_cost / units
    profit_per_unit = cost_per_unit * profit_margin
    selling_price = cost_per_unit + profit_per_unit
    result = selling_price
    return result

print(solution())