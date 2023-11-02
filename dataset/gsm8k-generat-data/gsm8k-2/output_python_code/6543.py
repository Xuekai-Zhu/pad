def solution():
    """George donated half his monthly income to charity and spent $20 from the other half on groceries. If he now has $100 left, how much was his monthly income?"""
    remaining_money = 100
    grocery_spending = 20
    donated_money = (remaining_money + grocery_spending) * 0.5
    monthly_income = donated_money + remaining_money + grocery_spending
    result = monthly_income
    return result

print(solution())