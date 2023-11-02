def solution():
    
    total_cost = 150
    packs_of_gummy_bears = 10
    cost_of_gummy_bears = 2
    bags_of_chocolate_chips = 20
    cost_of_chocolate_chips = 5
    cost_of_chocolate_bars = (total_cost - (packs_of_gummy_bears * cost_of_gummy_bears) - (bags_of_chocolate_chips * cost_of_chocolate_chips)) / 10
    result = cost_of_chocolate_bars
    return result

print(solution())