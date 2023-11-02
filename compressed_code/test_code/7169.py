def solution():
    
    num_employees = 500 + 200
    wage_per_hour = 12
    hours_per_day = 10
    days_per_week = 5
    weeks_per_month = 4
    total_hours_per_month = num_employees * hours_per_day * days_per_week * weeks_per_month
    total_pay_per_month = total_hours_per_month * wage_per_hour
    result = total_pay_per_month
    return result

print(solution())