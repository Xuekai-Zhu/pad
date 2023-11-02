def solution():
    num_games = 5
    found_tickets = 5
    ticket_value = 3
    total_value = 30

    # Calculate the total number of tickets Taegan has
    total_tickets = (total_value / ticket_value) - found_tickets

    # Calculate the number of tickets Taegan won from each game
    tickets_per_game = total_tickets / num_games
    result = tickets_per_game
    return result

print(solution())