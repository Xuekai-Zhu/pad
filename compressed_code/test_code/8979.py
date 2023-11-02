def solution():
    
    hourly_wage = 10
    overtime_wage = 15
    regular_hours = 40
    overtime_hours = 60 - regular_hours
    regular_pay = regular_hours * hourly_wage
    overtime_pay = overtime_hours * overtime_wage
    total_pay = regular_pay + overtime_pay
    result = total_pay
    
    return result

print(solution())