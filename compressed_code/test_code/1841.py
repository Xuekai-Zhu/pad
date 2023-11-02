def solution():
    
    oranges = 25
    cost = 1250 
    selling_price = 60 
    revenue = selling_price * oranges
    profit = revenue - cost
    profit_per_orange = profit / oranges
    result = profit_per_orange
    return result

print(solution())