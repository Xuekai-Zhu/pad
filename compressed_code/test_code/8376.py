def solution():
    
    seeds_per_bag = 100
    cost_per_bag = 0.5
    price_per_ear = 0.1
    
    
    profit_per_ear = price_per_ear - (cost_per_bag / seeds_per_bag) * 4
    
    
    total_profit = 40
    ears_sold = total_profit / profit_per_ear
    
    result = ears_sold
    return result

print(solution())