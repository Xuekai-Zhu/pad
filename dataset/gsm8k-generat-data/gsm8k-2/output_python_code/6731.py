def solution():
    """Nancy's ex owes her child support. He's supposed to pay 30% of his income each year. 
    For 3 years, he made $30,000/year, then he got a 20% raise for the next four years. 
    If he's only ever paid $1,200, how much does he owe her?"""
    income_3_years = 3 * 30000
    income_4_years = 4 * 1.2 * income_3_years
    total_income = income_3_years + income_4_years
    total_owed = 0.3 * total_income
    amount_paid = 1200
    amount_owed = total_owed - amount_paid
    result = amount_owed
    return result

print(solution())