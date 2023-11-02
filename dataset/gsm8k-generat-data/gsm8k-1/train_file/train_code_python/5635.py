def solution():
    """Dakota and Ben order eggs for $3, pancakes for $2, and 2 mugs of cocoa for $2 each. The tax is $1. Later, Ben then decides to order 1 more batch of pancakes and 1 more mug of cocoa as he is still hungry. How much change should they get from $15?"""
    cost_1 = 3 + 2 + (2 * 2)
    cost_2 = cost_1 + 2 + 2
    total_cost = cost_2 + 1
    change = 15 - total_cost
    result = change
    return result

print(solution())