def solution():
    
    plates_cost = 9 * 2
    total_cost = 24
    spoons_cost = total_cost - plates_cost
    spoons_bought = spoons_cost / 1.5
    result = spoons_bought
    return result

print(solution())