def solution():
    """Marie is planning to buy a new cash register for her bakery that costs $1040. Every day Marie sells 40 loaves of bread for $2 each and 6 cakes for $12 each. She has to pay $20 each day for rent and $2 each day for electricity. How many days' worth of profits will it take for Marie to pay for the cash register?"""
    # Define the cost of the cash register
    cash_register_cost = 1040

    # Define the daily sales of loaves of bread and cakes, and the daily expenses
    daily_bread_sales = 40 * 2
    daily_cake_sales = 6 * 12
    daily_expenses = 20 + 2

    # Calculate the daily profit
    daily_profit = daily_bread_sales + daily_cake_sales - daily_expenses

    # Calculate the number of days it will take to pay for the cash register
    days_to_pay = cash_register_cost / daily_profit

    result = round(days_to_pay)
    return result

print(solution())