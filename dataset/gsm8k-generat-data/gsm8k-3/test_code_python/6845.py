def solution():
    """A vendor bought apples at 2 for $3 and plans to sell them at 5 for $10. He also bought 3 oranges for $2.70 and plans to sell them at $1 each. How much is his profit if he sells 5 apples and 5 oranges?"""
    # Define the cost and selling prices of apples and oranges
    APPLE_COST = 1.5 # 2 apples for $3
    APPLE_PRICE = 2 # 5 apples for $10
    ORANGE_COST = 0.9 # 3 oranges for $2.70
    ORANGE_PRICE = 1 # 1 orange for $1

    # Calculate the cost and selling price of 5 apples
    apple_cost = 5/2 * APPLE_COST
    apple_price = 5 * APPLE_PRICE

    # Calculate the cost and selling price of 5 oranges
    orange_cost = 5 * ORANGE_COST
    orange_price = 5 * ORANGE_PRICE

    # Calculate the total cost and total revenue
    total_cost = apple_cost + orange_cost
    total_revenue = apple_price + orange_price

    # Calculate the profit
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())