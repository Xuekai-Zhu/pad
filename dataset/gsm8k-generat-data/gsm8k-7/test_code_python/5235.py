def solution():
    mr_banks_income_per_investment = 500
    num_mr_banks_investments = 8

    ms_elizabeth_income_per_investment = 900
    num_ms_elizabeth_investments = 5

    # Calculate the total income of Mr. Banks
    total_mr_banks_income = mr_banks_income_per_investment * num_mr_banks_investments

    # Calculate the total income of Ms. Elizabeth
    total_ms_elizabeth_income = ms_elizabeth_income_per_investment * num_ms_elizabeth_investments

    # Calculate the difference in income between the two entrepreneurs
    income_difference = total_ms_elizabeth_income - total_mr_banks_income
    result = income_difference
    return result

print(solution())