def solution():
    """Nancy's ex owes her child support. He's supposed to pay 30% of his income each year. For 3 years, he made $30,000/year, then he got a 20% raise for the next four years. If he's only ever paid $1,200, how much does he owe her?"""
    # Calculate the total income for the first 3 years
    income_3_years = 3 * 30000

    # Calculate the total income for the next 4 years after the raise
    income_4_years = (4 * 30000) * 1.2

    # Calculate the total income for all 7 years
    total_income = income_3_years + income_4_years

    # Calculate the total child support owed
    child_support_owed = total_income * 0.3

    # Calculate the amount still owed after previous payments
    amount_owed = child_support_owed - 1200

    # Display the amount still owed
    result = amount_owed
    return result

print(solution())