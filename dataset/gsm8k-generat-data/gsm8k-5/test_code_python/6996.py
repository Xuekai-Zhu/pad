def solution():
    hourly_raise = 0.5  # Bob gets a raise of $0.50/hour
    weekly_hours = 40  # Bob works 40 hours a week
    housing_reduction = 60  # Bob's housing benefit is reduced by $60/month

    # Calculate Bob's new hourly wage
    new_hourly_wage = 20 + hourly_raise  # Bob currently earns $20/hour

    # Calculate Bob's new monthly housing benefit
    new_housing_benefit = 800 - housing_reduction  # Bob currently gets $800/month in housing benefit

    # Calculate Bob's new weekly earnings
    new_weekly_earnings = new_hourly_wage * weekly_hours

    # Calculate Bob's actual new weekly earnings after accounting for the reduced housing benefit
    actual_new_earnings = new_weekly_earnings - (housing_reduction / 4)  # There are 4 weeks in a month

    # Calculate how much more Bob will earn per week
    more_earnings_per_week = actual_new_earnings - (20 * 40)  # Bob currently earns $20/hour and works 40 hours a week

    result = more_earnings_per_week
    return result

print(solution())