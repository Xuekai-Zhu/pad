def solution():
    # Calculate ex's income for the first 3 years
    income_first_three_years = 30000 * 3

    # Calculate ex's income for the next 4 years after the raise
    income_next_four_years = 36000 * 4  # 20% raise from $30,000 is $36,000

    # Calculate the total income for 7 years
    total_income = income_first_three_years + income_next_four_years

    # Calculate the total amount owed to Nancy
    amount_owed = total_income * 0.3  # ex is supposed to pay 30% of his income

    # Calculate the remaining amount owed after deducting what he's already paid
    remaining_amount = amount_owed - 1200

    result = remaining_amount
    return result

print(solution())