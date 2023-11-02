def solution():
    
    parts_cost = 20 * 2
    total_labor_cost = 220 - parts_cost
    labor_rate = 0.5
    total_labor_time_minutes = total_labor_cost / labor_rate
    total_labor_time_hours = total_labor_time_minutes / 60
    result = total_labor_time_hours
    return result

print(solution())