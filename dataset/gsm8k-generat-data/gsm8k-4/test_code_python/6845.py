def solution():
    """A vendor bought apples at 2 for $3 and plans to sell them at 5 for $10. He also bought 3 oranges for $2.70 and plans to sell them at $1 each. How much is his profit if he sells 5 apples and 5 oranges?"""
    # Define the cost and selling prices of apples
    apple_cost = 1.50 # 2 apples for $3 means 1 apple costs $1.50
    apple_sell = 2.00 # 5 apples for $10 means 1 apple is sold for $2.00

    # Define the cost and selling prices of oranges
    orange_cost = 0.90 # 3 oranges for $2.70 means 1 orange costs $0.90
    orange_sell = 1.00 # 1 orange is sold for $1.00

    # Calculate the total cost and selling prices of 5 apples and 5 oranges
    total_cost = (5 * apple_cost) + (5 * orange_cost)
    total_sell = (5 * apple_sell) + (5 * orange_sell)

    # Calculate the profit
    profit = total_sell - total_cost

    result = profit
    return result

print(solution())