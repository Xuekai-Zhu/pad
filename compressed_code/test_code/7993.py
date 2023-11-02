def solution():
    
    money_in_pocket = 15
    notebooks_cost = 4 * 2
    pens_cost = 1.5 * 2
    total_cost = notebooks_cost + pens_cost
    money_left = money_in_pocket - total_cost
    result = money_left
    return result

print(solution())