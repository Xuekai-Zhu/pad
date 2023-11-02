def solution():
    """A movie ticket costs $5. The cost of the popcorn is 80% of the cost of the ticket and a can of soda costs 50% of the cost of the popcorn. A family bought 4 tickets, 2 sets of popcorn, and 4 cans of soda. How much did they spend?"""
    ticket_cost = 5
    popcorn_cost = 0.8 * ticket_cost
    soda_cost = 0.5 * popcorn_cost
    total_cost = (4 * ticket_cost) + (2 * popcorn_cost) + (4 * soda_cost)
    result = total_cost
    return result

print(solution())