def solution():
    cost_per_dozen = 2.40
    sell_price_per_donut = 1
    goal = 96
    donuts_needed = goal / sell_price_per_donut
    dozens_needed = donuts_needed / 12
    result = dozens_needed
    
    return result

print(solution())