def solution():
    """A teacher teaches 5 periods a day and works 24 days a month. He is paid $5 per period. if he has been working for 6 months now how much has he earned in total?"""
    periods_per_day = 5
    days_per_month = 24
    pay_per_period = 5
    work_months = 6
    total_periods = periods_per_day * days_per_month * work_months
    total_pay = total_periods * pay_per_period
    result = total_pay
    return result

print(solution())