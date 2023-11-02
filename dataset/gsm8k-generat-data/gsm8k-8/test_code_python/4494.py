def solution():
    # Calculate the total amount of allowance Thomas received in the first year
    allowance_year_1 = 50 * 52

    # Calculate the total amount of income Thomas earned in the second year
    income_year_2 = 9 * 30 * 52

    # Calculate the total amount of money Thomas spent on himself during the 2 years
    total_spending = 35 * (52 * 2)

    # Calculate Thomas' total savings after 2 years
    total_savings = allowance_year_1 + income_year_2 - total_spending

    # Calculate the amount of money Thomas still needs to buy the car
    money_needed = 15000 - total_savings
    result = money_needed
    return result

print(solution())