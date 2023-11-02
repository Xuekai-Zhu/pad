def solution():
    
    rent = 1200
    utilities = rent * 0.2
    employees_per_shift = 2
    hours_per_day = 16
    days_per_week = 5
    hourly_wage = 12.5
    weekly_wages = employees_per_shift * hours_per_day * days_per_week * hourly_wage
    total_expenses = rent + utilities + weekly_wages
    result = total_expenses
    return result

print(solution())