def solution():
    # Calculate the total number of tickets Taegan has
    total_tickets = 5 + 5  # she wins tickets from 5 carnival games and finds 5 tickets on the floor
    ticket_value = 3  # each ticket is worth $3
    total_value = ticket_value * total_tickets  # total value of all the tickets
    equal_value = total_value / 5  # if Taegan won an equal number of tickets from each game, the value from each game would be the same
    equal_tickets = equal_value / ticket_value  # number of tickets Taegan won from each game

    result = equal_tickets
    return result

print(solution())