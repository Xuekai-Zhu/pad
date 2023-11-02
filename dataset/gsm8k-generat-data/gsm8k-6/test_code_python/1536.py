def solution():
    # Calculate the cost of 4 movie tickets
    ticket_cost = 5 * 4

    # Calculate the cost of 2 sets of popcorn
    popcorn_cost = 0.8 * ticket_cost * 2

    # Calculate the cost of 4 cans of soda
    soda_cost = 0.5 * popcorn_cost * 4

    # Calculate the total cost
    total_cost = ticket_cost + popcorn_cost + soda_cost
    result = total_cost
    return result

print(solution())