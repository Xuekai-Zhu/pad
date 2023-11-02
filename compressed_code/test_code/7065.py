def solution():
    
    pork_price = 6
    chicken_price = pork_price - 2
    pork_weight = 1
    chicken_weight = 3
    total_cost = (pork_price * pork_weight) + (chicken_price * chicken_weight)
    result = total_cost
    return result

print(solution())