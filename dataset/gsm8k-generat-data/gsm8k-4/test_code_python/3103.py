def solution():
    """Taegan goes to a carnival where she wins tickets from each of the 5 carnival games and also finds 5 tickets on the floor. Each ticket is worth $3. In total, she has tickets that total a value of $30. If Taegan won an equal number of tickets from each of the games, how many tickets did she win from each game?"""
    # Define the number of games and the value of each ticket
    NUM_GAMES = 5
    TICKET_VALUE = 3

    # Calculate the total value of tickets Taegan has
    total_value = 30

    # Subtract the value of the found tickets
    total_value -= TICKET_VALUE * 5

    # Calculate the value of tickets won from each game
    game_value = total_value / NUM_GAMES

    # Calculate the number of tickets won from each game
    num_tickets = game_value / TICKET_VALUE

    result = int(num_tickets)
    return result

print(solution())