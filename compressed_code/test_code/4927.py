def solution():
    
    hourly_rate = 60
    hours_per_day = 8
    days_worked = 14
    total_hours = hours_per_day * days_worked
    labor_cost = total_hours * hourly_rate
    parts_cost = 2500
    total_cost = labor_cost + parts_cost
    result = total_cost
    return result

print(solution())