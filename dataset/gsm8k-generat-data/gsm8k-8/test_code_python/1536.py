def solution():
    # Calculate the cost of one ticket
    ticket_cost = 5

    # Calculate the cost of one popcorn
    popcorn_cost = 0.8 * ticket_cost

    # Calculate the cost of one soda
    soda_cost = 0.5 * popcorn_cost

    # Calculate the total cost of tickets
    total_ticket_cost = 4 * ticket_cost

    # Calculate the total cost of popcorn
    total_popcorn_cost = 2 * popcorn_cost

    # Calculate the total cost of soda
    total_soda_cost = 4 * soda_cost

    # Calculate the total amount spent
    total_spent = total_ticket_cost + total_popcorn_cost + total_soda_cost
    result = total_spent
    return result

print(solution())