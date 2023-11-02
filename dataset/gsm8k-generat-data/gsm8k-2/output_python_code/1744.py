def solution():
    """There are two babysitters named Mila and Agnes. Mila makes $10 an hour while Agnes makes $15 an hour. Agnes works 8 hours each week. How many hours does Mila need to work to earn as much as Agnes in a month?"""
    agnes_weekly_earnings = 15 * 8
    monthly_earnings_agnes = agnes_weekly_earnings * 4
    hourly_rate_mila = 10
    hours_needed_mila = monthly_earnings_agnes / hourly_rate_mila
    result = hours_needed_mila
    return result

print(solution())