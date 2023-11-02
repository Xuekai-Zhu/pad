def solution():
    cans_collected = 20
    bottle_weight = 6
    can_weight = 2
    max_weight = 100
    bottles_collected = (max_weight - (cans_collected * can_weight)) / bottle_weight
    money_made = (bottles_collected * .1) + (cans_collected * .03)
    result = money_made
    
    return result

print(solution())