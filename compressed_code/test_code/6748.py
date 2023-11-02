def solution():
    
    hours_per_day = 8
    wage_per_hour = 7.50
    days_per_month = 20
    months_worked = 2
    total_hours_worked = hours_per_day * days_per_month * months_worked
    total_earnings = total_hours_worked * wage_per_hour
    result = total_earnings
    return result

print(solution())