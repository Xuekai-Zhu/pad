def solution():
    
    apples_cost = 40
    pears_cost = 50
    dozen_in_order = 14
    total_apples_cost = apples_cost * dozen_in_order
    total_pears_cost = pears_cost * dozen_in_order
    total_cost = total_apples_cost + total_pears_cost
    result = total_cost
    return result

print(solution())