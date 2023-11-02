def solution():
    """Paul went to a shop to buy some groceries. He bought some bread for $2, butter for $3, and juice for two times the price of the bread. He had $15 for his shopping. How much money did Paul have left?"""
    bread_price = 2
    butter_price = 3
    juice_price = 2 * bread_price
    total_price = bread_price + butter_price + juice_price
    money_left = 15 - total_price
    result = money_left
    return result

print(solution())