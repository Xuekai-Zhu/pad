def solution():
    """Paul went to a shop to buy some groceries. He bought some bread for $2, butter for $3, and juice for two times the price of the bread. He had $15 for his shopping. How much money did Paul have left?"""
    # Define the prices of bread, butter, and juice
    bread_price = 2
    butter_price = 3
    juice_price = bread_price * 2

    # Define the available budget for shopping
    total_budget = 15

    # Calculate the total cost of shopping
    total_cost = bread_price + butter_price + juice_price

    # Calculate the amount of money Paul has left
    money_left = total_budget - total_cost

    # Return the result
    result = money_left
    return result

print(solution())