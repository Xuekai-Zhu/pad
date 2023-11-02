def solution():
    
    hourly_wage_employee_1 = 20
    hourly_wage_employee_2 = 22
    hourly_subsidy_employee_2 = 6
    hours_per_week = 40
    weekly_wage_employee_1 = hourly_wage_employee_1 * hours_per_week
    weekly_wage_employee_2 = (hourly_wage_employee_2 - hourly_subsidy_employee_2) * hours_per_week
    weekly_savings = weekly_wage_employee_1 - weekly_wage_employee_2
    result = weekly_savings
    return result

print(solution())