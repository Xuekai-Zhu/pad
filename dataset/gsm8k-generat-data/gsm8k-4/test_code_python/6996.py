def solution():
    """Bob gets rent assistance because he's low-income. If he gets a raise of $0.50/hour and works 40 hours a week, how much more will he actually earn a week if his housing benefit is reduced by $60/month?"""
    # Define the raise per hour and the number of hours worked per week
    raise_per_hour = 0.5
    hours_per_week = 40

    # Calculate the increase in weekly earnings from the raise
    raise_weekly_increase = raise_per_hour * hours_per_week

    # Calculate the reduction in housing benefit per week
    housing_benefit_reduction = 60 / 4.33

    # Calculate the net increase in weekly earnings
    net_weekly_increase = raise_weekly_increase - housing_benefit_reduction

    result = net_weekly_increase
    return result

print(solution())