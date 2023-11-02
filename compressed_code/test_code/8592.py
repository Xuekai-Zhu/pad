def solution():
    
    biscuits_per_day = 4
    bones_per_day = 2
    cost_per_biscuit = 0.25
    cost_per_bone = 1
    days_per_week = 7
    total_cost = (biscuits_per_day * cost_per_biscuit + bones_per_day * cost_per_bone) * days_per_week
    result = total_cost
    return result

print(solution())