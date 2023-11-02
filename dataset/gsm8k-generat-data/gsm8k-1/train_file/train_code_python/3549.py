def solution():
    """Porter earns $8 per day and works 5 times a week. His manager is asking him to work an extra day that promises him an extra fifty percent on top of his daily rate. How much money will he earn after a month if he renders overtime every week?"""
    daily_rate = 8
    overtime_rate = daily_rate * 1.5
    weekly_hours = 6 * 8
    weekly_pay = (daily_rate * 5 * 8) + (overtime_rate * 8)
    monthly_pay = weekly_pay * 4
    result = monthly_pay
    return result

print(solution())