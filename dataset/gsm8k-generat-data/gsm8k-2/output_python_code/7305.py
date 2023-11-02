def solution():
    """Roxanne bought 2 cups of lemonade for $2 each and 2 sandwiches for $2.50 each. How much change must she get from a $20 bill?"""
    lemonade_cost = 2 * 2
    sandwich_cost = 2 * 2.5
    total_cost = lemonade_cost + sandwich_cost
    change = 20 - total_cost
    result = change
    return result

print(solution())