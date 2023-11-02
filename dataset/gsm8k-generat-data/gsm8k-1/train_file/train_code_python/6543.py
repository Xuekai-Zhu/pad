def solution():
    """George donated half his monthly income to charity and spent $20 from the other half on groceries. If he now has $100 left, how much was his monthly income?"""
    money_left = 100
    spent_on_groceries = 20
    half_income = (money_left + spent_on_groceries) * 2
    monthly_income = half_income
    return monthly_income

print(solution())