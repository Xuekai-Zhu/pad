def solution():
    
    cost_per_dozen = 50
    selling_price_per_half_dozen = 30
    strawberries_per_dozen = 12
    strawberries_per_half_dozen = 6
    dozens_sold = 50

    cost_per_strawberry = cost_per_dozen / strawberries_per_dozen  
    revenue_per_half_dozen = selling_price_per_half_dozen  
    cost_per_half_dozen = cost_per_strawberry * strawberries_per_half_dozen  
    profit_per_half_dozen = revenue_per_half_dozen - cost_per_half_dozen  
    profit_per_dozen = 2 * profit_per_half_dozen  
    total_profit = profit_per_dozen * dozens_sold  

    result = total_profit
    return result

print(solution())