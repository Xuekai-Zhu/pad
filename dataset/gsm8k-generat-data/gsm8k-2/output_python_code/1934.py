def solution():
    """Reese had a sum of money in her savings account. The company she worked with was not doing well which is why she lost her job. So she spent 20% of her savings for expenses in February, 40% of it in March, and $1500 in April. How much did she have in her savings account if she still has $2900 after spending those amounts?"""
    remaining_amount = 2900
    april_expenses = 1500
    march_expenses = 0.4 * (remaining_amount + april_expenses)
    feb_expenses = 0.2 * (remaining_amount + march_expenses + april_expenses)
    total_expenses = april_expenses + march_expenses + feb_expenses
    initial_savings = remaining_amount + total_expenses
    result = initial_savings
    return result

print(solution())