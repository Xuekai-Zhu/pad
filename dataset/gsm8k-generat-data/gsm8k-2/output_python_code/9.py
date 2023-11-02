def solution():
    """Tina makes $18.00 an hour. If she works more than 8 hours per shift, she is eligible for overtime, which is paid by your hourly wage + 1/2 your hourly wage. If she works 10 hours every day for 5 days, how much money does she make?"""
    wage_per_hour = 18.00
    regular_hours_per_day = 8
    overtime_hours_per_day = 2
    overtime_rate = 1.5
    days_worked = 5

    regular_pay_per_day = wage_per_hour * regular_hours_per_day
    overtime_pay_per_day = (wage_per_hour * overtime_rate) * overtime_hours_per_day
    daily_pay = regular_pay_per_day + overtime_pay_per_day
    total_pay = daily_pay * days_worked

    result = total_pay
    return result

print(solution())