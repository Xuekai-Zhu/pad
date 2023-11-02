def solution():
    """Todd has $20. He buys 4 candy bars that cost $2 each. How much money in dollars does Todd have left?"""
    todd_money = 20
    candy_bar_cost = 2
    num_candy_bars = 4
    total_spent = candy_bar_cost * num_candy_bars
    money_left = todd_money - total_spent
    result = money_left
    return result

print(solution())