def solution():
    # Define the hourly wage and hours worked per week
    hourly_wage = 10
    new_hourly_wage = 10.5
    hours_per_week = 40

    # Calculate the weekly earnings before and after the raise
    weekly_earnings_before = hourly_wage * hours_per_week
    weekly_earnings_after = new_hourly_wage * hours_per_week

    # Calculate the total reduction in housing benefit per week
    housing_benefit_reduction_per_week = 60 / 4.35

    # Calculate the net increase in weekly earnings
    net_increase = weekly_earnings_after - weekly_earnings_before - housing_benefit_reduction_per_week
    result = net_increase
    return result

print(solution())