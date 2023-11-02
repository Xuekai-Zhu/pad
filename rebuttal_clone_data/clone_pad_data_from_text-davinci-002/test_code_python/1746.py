def solution():
    regular_employees = 500
    extra_employees = 200
    regular_hours = 10
    extra_hours = regular_hours + 2
    days_worked = 5
    weeks_in_month = 4
    hourly_rate = 12
    regular_monthly_salary = regular_employees * regular_hours * hourly_rate * days_worked * weeks_in_month
    extra_monthly_salary = extra_employees * extra_hours * hourly_rate * days_worked * weeks_in_month
    total_monthly_salary = regular_monthly_salary + extra_monthly_salary
    
    return total_monthly_salary

print(solution())