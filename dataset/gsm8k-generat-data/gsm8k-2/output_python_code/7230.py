def solution():
    """Tyler has $100. If he buys 8 scissors for $5 each and 10 erasers for $4 each, how much of his money remains?"""
    total_scissors_cost = 8 * 5
    total_erasers_cost = 10 * 4
    total_cost = total_scissors_cost + total_erasers_cost
    remaining_money = 100 - total_cost
    result = remaining_money
    return result

print(solution())