def solution():
    """A carnival snack booth made $50 selling popcorn each day. It made three times as much selling cotton candy.
    For a 5-day activity, the booth has to pay $30 rent and $75 for the cost of ingredients.
    How much did the booth earn for 5 days after paying the rent and the cost of ingredients?"""
    popcorn_sales = 50 * 5
    cotton_candy_sales = 3 * 50 * 5
    total_sales = popcorn_sales + cotton_candy_sales
    expenses = 30 + 75
    earnings = total_sales - expenses
    result = earnings
    return result

print(solution())