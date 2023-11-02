def solution():
    """Paul went to a shop to buy some groceries. He bought some bread for $2, butter for $3, and juice for two times the price of the bread. He had $15 for his shopping. How much money did Paul have left?"""
    # Define the prices of bread, butter and juice
    bread_price = 2
    butter_price = 3
    juice_price = 2 * bread_price

    # Define the total amount of money Paul spent
    total_spent = bread_price + butter_price + juice_price

    # Calculate the amount of money Paul had left
    money_left = 15 - total_spent

    # Display the amount of money Paul had left
    result = money_left
    return result

print(solution())