def solution():
    """Kim spends $25,000 to open a store. She makes $4000 a month in revenue and her expenses are $1500 a month. How long would it take to pay back the cost to open the store?"""
    opening_cost = 25000
    monthly_revenue = 4000
    monthly_expenses = 1500
    monthly_profit = monthly_revenue - monthly_expenses
    months_to_repay = opening_cost / monthly_profit
    result = months_to_repay
    return result

print(solution())