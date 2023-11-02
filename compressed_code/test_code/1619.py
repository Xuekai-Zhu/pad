def solution():
    
    cost_per_can = 10
    can_size = 5
    daily_consumption = 6 
    weekly_consumption = daily_consumption * 7
    cans_per_week = weekly_consumption / can_size
    total_cost = cans_per_week * cost_per_can
    result = total_cost
    return result

print(solution())