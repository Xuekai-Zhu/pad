def solution():
    
    periods_per_day = 5
    days_per_month = 24
    pay_per_period = 5
    months_worked = 6
    total_periods = periods_per_day * days_per_month * months_worked
    total_pay = total_periods * pay_per_period
    result = total_pay
    return result

print(solution())