def solution():
    
    call_duration = 30
    cost_per_minute = 0.05
    calls_per_week = 1
    weeks_per_year = 52
    total_duration = call_duration * calls_per_week * weeks_per_year
    total_cost = total_duration * cost_per_minute
    result = total_cost
    return result

print(solution())