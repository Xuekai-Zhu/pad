def solution():
    """Amy's grandfather gave her $100 for her birthday. Amy bought 3 dolls, each of which cost $1. How much money does Amy have left?"""
    starting_money = 100
    dolls_cost = 3
    dolls_price = 1
    money_left = starting_money - (dolls_cost * dolls_price)
    result = money_left
    return result

print(solution())