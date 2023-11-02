def solution():
    
    tv_cost = 1700
    weekly_hours = 30
    hourly_rate = 10
    monthly_income = weekly_hours * hourly_rate * 4
    extra_income_needed = tv_cost - monthly_income
    hours_needed = extra_income_needed / hourly_rate
    result = hours_needed
    return result

print(solution())