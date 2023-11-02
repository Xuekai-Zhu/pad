def solution():
    
    total_profit = 96
    cost_per_dozen = 2.4
    revenue_per_donut = 1
    donuts_per_dozen = 12
    
    
    profit_per_dozen = (revenue_per_donut * donuts_per_dozen) - cost_per_dozen
    
    
    dozens_needed = total_profit / profit_per_dozen
    
    result = dozens_needed
    return result

print(solution())