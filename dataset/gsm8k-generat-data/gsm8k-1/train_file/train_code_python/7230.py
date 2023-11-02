def solution():
    """Tyler has $100. If he buys 8 scissors for $5 each and 10 erasers for $4 each, how much of his money remains?"""
    starting_money = 100
    num_scissors = 8
    cost_per_scissor = 5
    num_erasers = 10
    cost_per_eraser = 4
    total_spent = (num_scissors * cost_per_scissor) + (num_erasers * cost_per_eraser)
    remaining_money = starting_money - total_spent
    result = remaining_money
    return result

print(solution())