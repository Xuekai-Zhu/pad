def solution():
    
    cost_per_pie = 0.5
    price_per_piece = 4
    pieces_per_pie = 3
    pies_per_hour = 12
    total_profit = (price_per_piece * pieces_per_pie - cost_per_pie) * pies_per_hour
    result = total_profit
    return result

print(solution())