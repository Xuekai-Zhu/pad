def solution():
    
    wands_bought = 3
    wands_sold = 2
    profit_per_wand = 5
    total_profit = 130
    cost_per_wand = (total_profit / wands_sold) - profit_per_wand
    result = cost_per_wand
    return result

print(solution())