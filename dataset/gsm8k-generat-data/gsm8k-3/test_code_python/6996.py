def solution():
    """Bob gets rent assistance because he's low-income. If he gets a raise of
    $0.50/hour and works 40 hours a week, how much more will he actually earn
    a week if his housing benefit is reduced by $60/month?"""
    # Define the wage increase and housing benefit reduction
    WAGE_INCREASE = 0.5
    HOUSING_BENEFIT_REDUCTION = 60

    # Calculate the weekly wage increase
    weekly_wage_increase = WAGE_INCREASE * 40

    # Calculate the monthly housing benefit reduction
    monthly_housing_benefit_reduction = HOUSING_BENEFIT_REDUCTION * 12 / 52

    # Calculate the net weekly increase in earnings
    net_weekly_increase = weekly_wage_increase - monthly_housing_benefit_reduction

    # Display the net weekly increase in earnings
    result = net_weekly_increase
    return result

print(solution())