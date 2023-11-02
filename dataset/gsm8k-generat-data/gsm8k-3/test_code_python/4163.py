def solution():
    """Tom buys 20 shares of a stock that costs $3 each.  He sells 10 of those shares for $4 each.  The rest of the shares end up doubling in value.  How much profit does he make?"""
    # Define the initial cost and selling price per share
    INITIAL_PRICE = 3
    SELLING_PRICE = 4

    # Calculate the cost of the 20 shares
    total_cost = INITIAL_PRICE * 20

    # Calculate the revenue from selling 10 shares
    selling_revenue = SELLING_PRICE * 10

    # Calculate the value of the remaining 10 shares after doubling in value
    remaining_value = (INITIAL_PRICE * 2) * 10

    # Calculate the total revenue
    total_revenue = selling_revenue + remaining_value

    # Calculate the profit
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())