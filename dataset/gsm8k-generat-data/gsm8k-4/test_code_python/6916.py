def solution():
    """A store marks a book 30% above the cost. But during a sale, a 10% discount was given. If the book costs $50, what is the percent profit?"""
    # Define the cost and sale price of the book
    cost = 50
    sale_price = cost * 1.3 * 0.9

    # Calculate the profit
    profit = sale_price - cost

    # Calculate the percentage profit
    percentage_profit = (profit / cost) * 100

    # return the result
    result = percentage_profit
    return result

print(solution())