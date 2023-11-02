def solution():
    
    total_items = 40
    total_cost = 150
    gummy_bear_cost = 2
    chocolate_chip_cost = 5
    chocolate_bar_cost = (total_cost - (10 * gummy_bear_cost) - (20 * chocolate_chip_cost)) / 10
    result = chocolate_bar_cost
    return result

print(solution())