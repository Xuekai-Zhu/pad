def solution():
    """Joshua bought 25 oranges for $12.50. If he sells each one for 60c, how much profit in cents will he make on each orange?"""
    # Calculate the cost per orange
    cost_per_orange = 12.50 / 25

    # Calculate the revenue per orange
    revenue_per_orange = 0.60

    # Calculate the profit per orange
    profit_per_orange = revenue_per_orange - cost_per_orange

    # Convert the profit to cents
    profit_in_cents = profit_per_orange * 100

    # Display the profit in cents
    result = profit_in_cents
    return result

print(solution())