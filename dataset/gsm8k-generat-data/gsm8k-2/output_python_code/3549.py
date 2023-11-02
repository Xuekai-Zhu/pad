def solution():
    """Porter earns $8 per day and works 5 times a week. His manager is asking him to work an extra day that promises him an extra fifty percent on top of his daily rate. How much money will he earn after a month if he renders overtime every week?"""
    regular_daily_pay = 8
    overtime_daily_pay = regular_daily_pay * 1.5
    regular_weekly_pay = regular_daily_pay * 5
    overtime_weekly_pay = overtime_daily_pay * 1
    total_weekly_pay = regular_weekly_pay + overtime_weekly_pay
    total_monthly_pay = total_weekly_pay * 4
    result = total_monthly_pay
    return result

print(solution())