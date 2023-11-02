def solution():
    
    normal_wage = 12
    overtime_wage = normal_wage * 1.5
    total_earnings = 696
    regular_hours = 40
    overtime_hours = (total_earnings - (normal_wage * regular_hours)) / overtime_wage
    total_hours = regular_hours + overtime_hours
    result = total_hours
    return result

print(solution())