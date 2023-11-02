def solution():
    """A movie ticket costs $5. The cost of the popcorn is 80% of the cost of the ticket and a can of soda costs 50% of the cost of the popcorn. A family bought 4 tickets, 2 sets of popcorn, and 4 cans of soda. How much did they spend?"""
    # Define the cost of a movie ticket and the percentage of the ticket cost for popcorn and soda
    TICKET_COST = 5
    POPCORN_PERCENTAGE = 0.8
    SODA_PERCENTAGE = 0.5

    # Calculate the cost of popcorn and soda
    popcorn_cost = POPCORN_PERCENTAGE * TICKET_COST
    soda_cost = SODA_PERCENTAGE * popcorn_cost

    # Calculate the total cost for the family
    total_cost = (4 * TICKET_COST) + (2 * popcorn_cost) + (4 * soda_cost)

    # Display the total cost for the family
    result = total_cost
    return result

print(solution())