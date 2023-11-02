def solution():
    starting_tickets = 11  # Nathaniel starts with 11 tickets
    remaining_tickets = 3  # Nathaniel ends up with 3 tickets
    tickets_given_away = starting_tickets - remaining_tickets  # Nathaniel gave away this many tickets

    # Calculate the number of best friends Nathaniel has
    num_friends = tickets_given_away // 2
    result = num_friends
    return result

print(solution())