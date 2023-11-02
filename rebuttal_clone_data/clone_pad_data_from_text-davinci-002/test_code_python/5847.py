def solution():
    hourly_wage = 8.50
    hours_worked_per_day = 8
    days_worked_per_month = 20
    months_worked_per_year = 12
    total_hours_worked = hours_worked_per_day * days_worked_per_month * months_worked_per_year
    annual_salary = hourly_wage * total_hours_worked
    result = annual_salary
    return result

print(solution())