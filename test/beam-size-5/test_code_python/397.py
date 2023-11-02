def solution():
    
    weeks_per_month = 4
    days_per_week = 6
    pay_per_day = 50
    weeks_per_year = 12
    total_weeks = weeks_per_month * months_per_year
    total_days = days_per_week * weeks_per_year
    total_pay = total_weeks * pay_per_day * weeks_per_year
    result = total_pay
    return result

print(solution())