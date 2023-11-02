def solution():
    ticket_cost = 5  # A movie ticket costs $5
    popcorn_cost = ticket_cost * 0.8  # The cost of the popcorn is 80% of the ticket cost
    soda_cost = popcorn_cost * 0.5  # The cost of a can of soda is 50% of the popcorn cost

    # Calculate the total cost of the movie for the family
    total_cost = (4 * ticket_cost) + (2 * popcorn_cost) + (4 * soda_cost)
    result = total_cost
    return result

print(solution())