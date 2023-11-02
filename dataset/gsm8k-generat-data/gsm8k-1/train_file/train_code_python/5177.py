def solution():
    """Irene shares half of a small apple with her dog every day. A small apple weighs about 1/4 of a pound. She can currently buy apples for $2.00 a pound. How much will she spend so that she and her dog have enough apples to last for 2 weeks?"""
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