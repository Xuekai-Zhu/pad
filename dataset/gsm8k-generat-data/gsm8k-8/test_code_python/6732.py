def solution():
    # Calculate the total income for the first 3 years
    total_income_3_years = 3 * 30000

    # Calculate the total income for the next 4 years with the 20% raise
    income_4th_year = 1.2 * 30000
    total_income_next_4_years = 4 * income_4th_year

    # Calculate the total income over all 7 years
    total_income = total_income_3_years + total_income_next_4_years

    # Calculate the amount owed in child support
    child_support_owed = 0.3 * total_income

    # Calculate the remaining amount owed after previous payments
    remaining_amount_owed = child_support_owed - 1200

    result = remaining_amount_owed
    return result

print(solution())