def solution():
    """Marie is planning to buy a new cash register for her bakery that costs $1040. Every day Marie sells 40 loaves of bread for $2 each and 6 cakes for $12 each. She has to pay $20 each day for rent and $2 each day for electricity. How many days' worth of profits will it take for Marie to pay for the cash register?"""
    cash_register_cost = 1040
    daily_sales = (40 * 2) + (6 * 12)
    daily_expenses = 20 + 2
    daily_profit = daily_sales - daily_expenses
    days_to_pay_off = cash_register_cost / daily_profit
    result = days_to_pay_off
    return result

print(solution())