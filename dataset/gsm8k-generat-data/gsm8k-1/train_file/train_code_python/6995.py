def solution():
    """Bob gets rent assistance because he's low-income. If he gets a raise of $0.50/hour and works 40 hours a week, how much more will he actually earn a week if his housing benefit is reduced by $60/month?"""
    hourly_raise = 0.5
    hours_per_week = 40
    weekly_raise = hourly_raise * hours_per_week
    rent_reduction = 60
    net_increase = weekly_raise - (rent_reduction / 4)
    result = net_increase
    return result

print(solution())