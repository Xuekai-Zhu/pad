def solution():
    """Bob gets rent assistance because he's low-income. If he gets a raise of $0.50/hour and works 40 hours a week, how much more will he actually earn a week if his housing benefit is reduced by $60/month?"""
    hourly_raise = 0.5
    weekly_hours = 40
    weekly_raise = hourly_raise * weekly_hours
    monthly_reduction = 60
    weekly_reduction = monthly_reduction / 4
    actual_weekly_earnings_increase = weekly_raise - weekly_reduction
    result = actual_weekly_earnings_increase
    return result

print(solution())