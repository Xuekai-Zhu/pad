def solution():
    """A fast-food chain offers free delivery for a minimum purchase of $18. Danny ordered 2 quarter-pounder burgers for $3.20 each, 2 large fries that cost $1.90 each, and 2 milkshakes that cost $2.40 each. How much more worth of food should he order to avail of the free delivery?"""
    total_cost = (2 * 3.20) + (2 * 1.90) + (2 * 2.40)
    amount_needed = 18 - total_cost
    result = amount_needed
    return result

print(solution())