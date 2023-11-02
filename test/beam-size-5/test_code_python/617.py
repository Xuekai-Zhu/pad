def solution():
    
    weeks = 6
    hours_per_week = 2
    sessions_cost_per_hour = 125
    total_hours = weeks * hours_per_week * sessions_cost_per_hour
    total_cost = total_hours * sessions_cost_per_hour
    result = total_cost
    return result

print(solution())