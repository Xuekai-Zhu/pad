def solution():
    """Joshua bought 25 oranges for $12.50. If he sells each one for 60c, how much profit in cents will he make on each orange?"""
    # Define the cost per orange and the selling price per orange in cents
    cost_per_orange = 12.50 / 25
    selling_price_per_orange = 60

    # Calculate the profit per orange in cents
    profit_per_orange = (selling_price_per_orange - cost_per_orange) * 100

    # return the result
    result = profit_per_orange
    return result

print(solution())