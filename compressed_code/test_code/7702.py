def solution():
    
    pineapple_cost = 1.25
    pineapples_per_dozen = 12
    total_pineapples = pineapples_per_dozen
    shipping_cost = 21
    total_cost = total_pineapples * pineapple_cost + shipping_cost
    cost_per_pineapple = total_cost / total_pineapples
    result = cost_per_pineapple
    return result

print(solution())