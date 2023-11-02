def solution():
    """A fast-food chain offers free delivery for a minimum purchase of $18. Danny ordered 2 quarter-pounder burgers for $3.20 each, 2 large fries that cost $1.90 each, and 2 milkshakes that cost $2.40 each. How much more worth of food should he order to avail of the free delivery?"""
    # Calculate the total cost of Danny's order
    total_cost = 2 * 3.20 + 2 * 1.90 + 2 * 2.40

    # Calculate how much more Danny needs to spend to avail of free delivery
    remaining_cost = 18 - total_cost

    # Display the remaining cost
    result = remaining_cost
    return result

print(solution())