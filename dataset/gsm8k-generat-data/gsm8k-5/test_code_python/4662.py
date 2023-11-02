def solution():
    bike_cost = 100  # The cost of the bike is $100
    weekly_allowance = 5  # Zach's weekly allowance is $5
    parent_pay = 10  # Zach's parent will pay him an extra $10 to mow the lawn
    neighbor_pay = 7  # Zach's neighbor will pay him $7 per hour to babysit their son
    babysitting_hours = 2  # Zach will babysit his neighbor's son for 2 hours

    # Calculate Zach's total income for the week
    total_income = weekly_allowance + parent_pay + (babysitting_hours * neighbor_pay)

    # Calculate Zach's total savings
    total_savings = 65 + total_income

    # Calculate the remaining amount Zach needs to save to buy the bike
    remaining_amount = bike_cost - total_savings
    result = remaining_amount
    return result

print(solution())