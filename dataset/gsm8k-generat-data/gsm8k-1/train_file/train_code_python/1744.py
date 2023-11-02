def solution():
    """There are two babysitters named Mila and Agnes. Mila makes $10 an hour while Agnes makes $15 an hour. Agnes works 8 hours each week. How many hours does Mila need to work to earn as much as Agnes in a month?"""
    agnes_weekly_earnings = 15 * 8
    monthly_earnings = agnes_weekly_earnings * 4
    mila_hourly_rate = 10
    mila_hours_needed = monthly_earnings / mila_hourly_rate
    result = mila_hours_needed
    return result

print(solution())