def solution():
    
    pie_price = 4 
    pie_cost = 0.5
    pie_pieces = 3
    pies_per_hour = 12
    
    total_pie_pieces = pies_per_hour * pie_pieces
    total_pie_cost = pies_per_hour * pie_cost
    total_profit = total_pie_pieces * pie_price - total_pie_cost
    
    result = total_profit
    return result

print(solution())