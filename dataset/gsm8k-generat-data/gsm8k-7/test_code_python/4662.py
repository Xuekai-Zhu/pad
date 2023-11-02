def solution():
    bike_cost = 100
    weekly_allowance = 5
    extra_income = 10 + (7 * 2)  # $10 for mowing lawn, $7/hour for babysitting for 2 hours
    current_savings = 65

    # Calculate the total income Zach can earn before buying the bike
    total_income = weekly_allowance * 8  # 8 weeks until he can afford the bike with allowance alone
    total_income += extra_income

    # Calculate how much more money Zach needs to earn before he can buy the bike
    remaining_cost = bike_cost - current_savings - total_income
    result = remaining_cost
    return result

print(solution())