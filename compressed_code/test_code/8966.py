def solution():
    
    pops_price = 1.5
    pops_cost = 0.9
    pencils_price = 1.8
    pens_needed = 100
    money_needed = pens_needed * pencils_price
    pops_needed = money_needed / (pops_price - pops_cost)
    result = pops_needed
    return result

print(solution())