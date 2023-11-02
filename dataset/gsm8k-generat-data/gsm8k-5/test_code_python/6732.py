def solution():
    # Calculate the total income for the first 3 years
    income_first_three_years = 30000 * 3

    # Calculate the total income for the next four years with a 20% raise
    income_next_four_years = 30000 * 1.2 * 4

    # Calculate the total income for all 7 years
    total_income = income_first_three_years + income_next_four_years

    # Calculate the total child support owed
    total_child_support = total_income * 0.3 * 7

    # Calculate the amount already paid
    amount_paid = 1200

    # Calculate the remaining amount owed
    amount_owed = total_child_support - amount_paid
    result = amount_owed
    return result

print(solution())