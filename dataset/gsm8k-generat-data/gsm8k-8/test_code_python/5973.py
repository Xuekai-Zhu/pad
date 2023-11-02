def solution():
    # Define the initial number of tickets Nathaniel has
    initial_tickets = 11

    # Define the number of tickets remaining after giving away tickets to best friends
    remaining_tickets = 3

    # Define the number of tickets given away to best friends
    tickets_given_away = initial_tickets - remaining_tickets

    # Define the number of best friends Nathaniel has
    num_best_friends = tickets_given_away / 2
    result = num_best_friends
    return result

print(solution())