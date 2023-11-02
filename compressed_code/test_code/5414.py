def solution():
    
    hourly_raise = 0.5
    weekly_hours = 40
    weekly_raise = hourly_raise * weekly_hours
    monthly_reduction = 60
    weekly_reduction = monthly_reduction / 4
    actual_weekly_earnings_increase = weekly_raise - weekly_reduction
    result = actual_weekly_earnings_increase
    return result

print(solution())