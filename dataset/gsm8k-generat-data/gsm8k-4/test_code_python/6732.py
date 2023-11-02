def solution():
    """Nancy's ex owes her child support. He's supposed to pay 30% of his income each year. For 3 years, he made $30,000/year, then he got a 20% raise for the next four years. If he's only ever paid $1,200, how much does he owe her?"""
    # Calculate the total income for the first 3 years
    first_three_years_income = 3 * 30000

    # Calculate the total income for the next 4 years with the raise
    next_four_years_income = 4 * 30000 * 1.2

    # Calculate the total income over the 7 years
    total_income = first_three_years_income + next_four_years_income

    # Calculate the total amount owed in child support
    total_child_support = total_income * 0.3

    # Calculate the amount still owed
    amount_owed = total_child_support - 1200

    result = amount_owed
    return result

print(solution())