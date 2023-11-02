def solution():
    
    rent = 1200
    utilities = rent * 0.2
    total_rent = rent + utilities
    employees_per_shift = 2
    hours_per_day = 16
    days_per_week = 5
    total_hours_per_week = employees_per_shift * hours_per_day * days_per_week
    employee_salary = 12.5
    total_employee_salary = total_hours_per_week * employee_salary
    weekly_expenses = total_rent + total_employee_salary
    result = weekly_expenses
    return result

print(solution())