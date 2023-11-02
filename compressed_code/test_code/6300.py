def solution():
    
    carrots_per_day = 1
    pounds_per_year = carrots_per_day * 365 / 5
    cost_per_pound = 2
    total_cost = pounds_per_year * cost_per_pound
    result = total_cost
    return result

print(solution())