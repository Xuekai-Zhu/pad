def solution():
    
    regular_daily_pay = 8
    overtime_daily_pay = regular_daily_pay * 1.5
    regular_weekly_pay = regular_daily_pay * 5
    overtime_weekly_pay = overtime_daily_pay * 1
    total_weekly_pay = regular_weekly_pay + overtime_weekly_pay
    total_monthly_pay = total_weekly_pay * 4
    result = total_monthly_pay
    return result

print(solution())