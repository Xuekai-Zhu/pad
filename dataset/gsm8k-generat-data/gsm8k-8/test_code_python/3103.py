def solution():
    # Define the number of games Taegan played
    num_games = 5

    # Calculate the total number of tickets Taegan has
    total_tickets = (num_games * x) + 5

    # Calculate the value of the tickets
    ticket_value = 3

    # Calculate the total value of the tickets
    total_value = 30

    # Solve for x (the number of tickets won from each game)
    x = (total_value - 5*ticket_value) / num_games * ticket_value

    result = x
    return result

print(solution())