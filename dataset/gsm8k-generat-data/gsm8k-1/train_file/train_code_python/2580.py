def solution():
    """Kenneth has $50 to go to the store. Kenneth bought 2 baguettes and 2 bottles of water. Each baguette cost $2 and each bottle of water cost $1. How much money does Kenneth have left?"""
    initial_money = 50
    baguette_cost = 2
    water_cost = 1
    total_spent = (2 * baguette_cost) + (2 * water_cost)
    money_left = initial_money - total_spent
    result = money_left
    return result

print(solution())