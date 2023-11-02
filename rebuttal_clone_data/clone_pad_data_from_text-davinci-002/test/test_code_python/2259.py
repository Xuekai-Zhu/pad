def solution():
    weekly_rent = 1200
    utilities = 0.2 * weekly_rent
    employees_per_shift = 2
    hours_per_day = 16
    days_per_week = 5
    employee_hours_per_week = employees_per_shift * hours_per_day * days_per_week
    employee_wages = 12.50 * employee_hours_per_week
    weekly_expenses = weekly_rent + utilities + employee_wages
    result = weekly_expenses
    return result

print(solution())