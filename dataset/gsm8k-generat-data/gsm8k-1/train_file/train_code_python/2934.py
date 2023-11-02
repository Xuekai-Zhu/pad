def solution():
    """Edward had $17.80 to spend at the toy store. He bought 4 toy cars that cost $0.95 each and a race track that cost $6.00. How much money does Edward have left to buy more toys?"""
    initial_money = 17.80
    toys_cost = (4 * 0.95) + 6.00
    money_left = initial_money - toys_cost
    result = money_left
    return result

print(solution())