def solution():
    
    pumpkin_pies = 10
    pumpkin_cost = 3
    cherry_pies = 12
    cherry_cost = 5
    total_cost = (pumpkin_pies * pumpkin_cost) + (cherry_pies * cherry_cost)
    total_profit = 20
    total_pies = pumpkin_pies + cherry_pies
    price_per_pie = (total_cost + total_profit) / total_pies
    result = price_per_pie
    return result

print(solution())