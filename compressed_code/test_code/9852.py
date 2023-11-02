def solution():
    
    apples_per_day = 1/2
    weight_per_apple = 1/4
    days = 14
    cost_per_pound = 2
    total_apples_needed = apples_per_day * days * 2
    total_weight_needed = total_apples_needed * weight_per_apple
    cost = total_weight_needed * cost_per_pound
    result = cost
    
    return result

print(solution())