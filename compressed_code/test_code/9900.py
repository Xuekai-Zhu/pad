def solution():
    
    cost_price = 50  
    selling_price = 30  
    strawberries_per_dozen = 12
    strawberries_per_half_dozen = 6
    dozens_sold = 50

    total_cost = cost_price * dozens_sold
    total_revenue = selling_price * 2 * dozens_sold

    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())