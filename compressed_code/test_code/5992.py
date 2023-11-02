def solution():
    
    minutes_per_call = 60 
    cost_per_min = 0.05
    calls_per_week = 50
    total_minutes_per_week = calls_per_week * minutes_per_call
    cost_per_week = total_minutes_per_week * cost_per_min
    total_cost_in_a_month = cost_per_week * 4
    result = total_cost_in_a_month
    return result

print(solution())