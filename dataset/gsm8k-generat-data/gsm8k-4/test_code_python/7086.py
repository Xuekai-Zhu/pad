def solution():
    """A carnival snack booth made $50 selling popcorn each day. It made three times as much selling cotton candy. For a 5-day activity, the booth has to pay $30 rent and $75 for the cost of the ingredients. How much did the booth earn for 5 days after paying the rent and the cost of ingredients?"""
    # Define the price of popcorn and cotton candy
    popcorn_price = 50
    cotton_candy_price = popcorn_price * 3

    # Calculate the total revenue for 5 days
    total_revenue = (popcorn_price + cotton_candy_price) * 5

    # Calculate the total cost for 5 days
    total_cost = 30 + 75

    # Calculate the profit for 5 days
    profit = total_revenue - total_cost

    # return the result
    result = profit
    return result

print(solution())