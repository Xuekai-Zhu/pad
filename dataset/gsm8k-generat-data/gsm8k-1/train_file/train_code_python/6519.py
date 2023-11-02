def solution():
    """Doris earns $20 per hour by babysitting. She needs to earn at least $1200 for her monthly expenses. She can babysit for 3 hours every weekday and 5 hours on a Saturday. How many weeks does it take for Doris to earn enough to cover her monthly expenses?"""
    hourly_pay = 20
    monthly_expenses = 1200
    weekly_hours = 3*5 + 5
    weekly_earnings = hourly_pay * weekly_hours
    weeks_to_reach_expenses = int(monthly_expenses / weekly_earnings) + 1
    result = weeks_to_reach_expenses
    return result

print(solution())