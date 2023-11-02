def solution():
    """Marj has two $20 bills, three $5 bills, and $4.50 in loose coins in her wallet. If she buys a cake that costs $17.50, how much money will be left in her wallet?"""
    total_money = (2 * 20) + (3 * 5) + 4.5
    cake_cost = 17.5
    money_left = total_money - cake_cost
    result = money_left
    return result

print(solution())