def solution():
    """You have 32$ to spend on groceries. You buy a loaf of bread for 3$, a candy bar for 2$, and 1/3 of whats left on a Turkey. How much money do you have left?"""
    initial_money = 32
    bread_cost = 3
    candy_bar_cost = 2
    turkey_cost = (initial_money - bread_cost - candy_bar_cost) / 3
    remaining_money = initial_money - bread_cost - candy_bar_cost - turkey_cost
    result = remaining_money
    return result

print(solution())