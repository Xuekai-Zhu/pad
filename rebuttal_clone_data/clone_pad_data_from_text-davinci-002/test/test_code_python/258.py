def solution():
    total_earnings = 696
    normal_hourly_wage = 12
    overtime_hourly_wage = 18
    regular_hours = 40
    overtime_hours = (total_earnings - (regular_hours * normal_hourly_wage)) / overtime_hourly_wage
    total_hours = regular_hours + overtime_hours
    result = total_hours
    
    return result

print(solution())