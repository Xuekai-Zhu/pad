def solution():
    
    watts_per_day = 60 * 40
    watts_per_month = watts_per_day * 30
    cost_per_watt = 0.20
    total_cost = watts_per_month * cost_per_watt
    result = total_cost
    return result

print(solution())