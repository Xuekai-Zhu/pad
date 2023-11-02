def solution():
    
    weekly_hours = 35
    workdays = 5
    daily_hours = weekly_hours / workdays
    hourly_wage = 9
    daily_wage = daily_hours * hourly_wage
    result = daily_wage
    return result

print(solution())