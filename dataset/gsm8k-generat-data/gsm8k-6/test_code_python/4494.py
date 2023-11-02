def solution():
    # Calculate the total amount of money Thomas saved in the first year with his $50 weekly allowance
    total_savings_first_year = 50 * 52  # $50 allowance per week for 52 weeks in a year

    # Calculate the total amount of money Thomas earned in the second year with his job
    total_earnings_second_year = 9 * 30 * 52  # $9 per hour, 30 hours a week, for 52 weeks in a year

    # Calculate the total amount of money Thomas spent on himself in the second year
    total_spending_second_year = 35 * 52  # $35 per week for 52 weeks in a year

    # Calculate the total amount of money Thomas saved in the second year
    total_savings_second_year = total_earnings_second_year - total_spending_second_year

    # Calculate the total amount of money Thomas saved in the 2 years
    total_savings = total_savings_first_year + total_savings_second_year

    # Calculate the amount of money Thomas still needs to buy the car
    amount_needed = 15000 - total_savings

    result = amount_needed
    return result

print(solution())