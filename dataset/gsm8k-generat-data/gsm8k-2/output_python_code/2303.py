def solution():
    """Amy's grandfather gave her $100 for her birthday. Amy bought 3 dolls, each of which cost $1. How much money does Amy have left?"""
    gift_money = 100
    doll_cost = 1
    doll_quantity = 3
    total_spent = doll_cost * doll_quantity
    remaining_money = gift_money - total_spent
    result = remaining_money
    return result

print(solution())