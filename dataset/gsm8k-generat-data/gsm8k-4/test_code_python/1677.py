def solution():
    """A fast-food chain offers free delivery for a minimum purchase of $18. Danny ordered 2 quarter-pounder burgers for $3.20 each, 2 large fries that cost $1.90 each, and 2 milkshakes that cost $2.40 each. How much more worth of food should he order to avail of the free delivery?"""
    # Define the minimum purchase for free delivery
    MIN_PURCHASE = 18

    # Calculate the total cost of the food ordered
    total_cost = 2*3.2 + 2*1.9 + 2*2.4

    # Calculate the additional cost needed to avail of free delivery
    additional_cost = MIN_PURCHASE - total_cost

    # Return the result
    result = additional_cost
    return result

print(solution())