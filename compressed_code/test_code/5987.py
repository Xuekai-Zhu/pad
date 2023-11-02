def solution():
    
    weekdays_per_month = 20
    weekend_days_per_month = 8
    weekday_income = 600
    weekend_income = weekday_income * 2
    total_income = (weekdays_per_month * weekday_income) + (weekend_days_per_month * weekend_income)
    result = total_income
    return result

print(solution())