def solution():
    """Taegan goes to a carnival where she wins tickets from each of the 5 carnival games and also finds 5 tickets on the floor. Each ticket is worth $3. In total, she has tickets that total a value of $30. If Taegan won an equal number of tickets from each of the games, how many tickets did she win from each game?"""
    # Define the value of each ticket and the total value of all tickets
    TICKET_VALUE = 3
    TOTAL_VALUE = 30

    # Calculate the number of tickets Taegan found on the floor
    found_tickets = 5

    # Calculate the value of the tickets Taegan won from each game
    game_tickets_value = (TOTAL_VALUE - (found_tickets * TICKET_VALUE)) / 5

    # Calculate the number of tickets Taegan won from each game
    game_tickets = int(game_tickets_value / TICKET_VALUE)

    # Display the number of tickets Taegan won from each game
    result = game_tickets
    return result

print(solution())