def solution():
    
    hourly_wage = 18.00
    hours_worked_regular = 8
    hours_worked_overtime = 10 - hours_worked_regular
    hourly_wage_overtime = hourly_wage * 1.5
    total_hours_worked = (hours_worked_regular * 5) + (hours_worked_overtime * 5)
    total_regular_pay = hourly_wage * (hours_worked_regular * 5)
    total_overtime_pay = hourly_wage_overtime * (hours_worked_overtime * 5)
    total_pay = total_regular_pay + total_overtime_pay
    result = total_pay
    return result

print(solution())