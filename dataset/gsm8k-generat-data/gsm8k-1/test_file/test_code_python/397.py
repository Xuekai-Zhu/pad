def solution():
    """A builder works for 4 weeks every month and for 6 days every week. If he gets paid $50 every day, how much does he earn if he works for a year?"""
    weeks_in_month = 4
    days_in_week = 6
    pay_per_day = 50
    months_in_year = 12
    total_days_worked = weeks_in_month * days_in_week * months_in_year
    total_pay = total_days_worked * pay_per_day
    result = total_pay
    return result

print(solution())