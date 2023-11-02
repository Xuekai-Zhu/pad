def solution():
    hourly_wage = 30
    regular_hours = 40
    overtime_hours = 6
    overtime_pay = hourly_wage * 1.5
    total_hours = regular_hours + overtime_hours
    total_pay = (regular_hours * hourly_wage) + (overtime_hours * overtime_pay)
    result = total_pay
    
    return result

print(solution())