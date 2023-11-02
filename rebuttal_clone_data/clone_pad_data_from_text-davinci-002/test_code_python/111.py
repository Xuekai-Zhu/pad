def solution():
    """Paul went to a shop to buy some groceries. He bought some bread for $2, butter for $3, and juice for two times the price of the bread. He had $15 for his shopping. How much money did Paul have left?"""
    bread_cost = 2
    butter_cost = 3
    juice_cost = 2 * bread_cost
    total_cost = bread_cost + butter_cost + juice_cost
    money_left = 15 - total_cost
    result = money_left
    
    return result

print(solution())