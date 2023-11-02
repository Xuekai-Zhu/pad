def solution():
    """A carnival snack booth made $50 selling popcorn each day. It made three times as much selling cotton candy. For a 5-day activity, the booth has to pay $30 rent and $75 for the cost of the ingredients. How much did the booth earn for 5 days after paying the rent and the cost of ingredients?"""
    # Define the revenue from selling popcorn per day and the revenue from selling cotton candy per day
    POPCORN_REVENUE = 50
    COTTON_CANDY_REVENUE = 3 * POPCORN_REVENUE

    # Define the number of days of the activity, the rent, and the cost of ingredients
    DAYS = 5
    RENT = 30
    INGREDIENTS = 75

    # Calculate the total revenue
    total_revenue = (POPCORN_REVENUE + COTTON_CANDY_REVENUE) * DAYS

    # Calculate the net profit
    net_profit = total_revenue - RENT - INGREDIENTS

    # Display the net profit
    result = net_profit
    return result

print(solution())