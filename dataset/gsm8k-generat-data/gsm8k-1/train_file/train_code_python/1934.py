def solution():
    """Reese had a sum of money in her savings account. The company she used to work with was not doing well which is why she lost her job. So she spent 20% of her savings for her expenses in February, 40% of it in March, and $1500 in April. How much did she have in her savings account if she still has $2900 after spending those amounts?"""
    remaining_amount = 2900
    april_spending = 1500
    march_spending = 0.4 * (remaining_amount + april_spending)
    feb_spending = 0.2 * (remaining_amount + april_spending + march_spending)
    total_spending = april_spending + march_spending + feb_spending
    start_amount = remaining_amount + total_spending
    result = start_amount
    return result

print(solution())