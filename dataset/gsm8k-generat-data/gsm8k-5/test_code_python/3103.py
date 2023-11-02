def solution():
    # Total number of tickets Taegan has
    total_tickets = (5 * equal_tickets) + 5

    # Total value of all tickets
    total_value = total_tickets * ticket_value

    # Calculate the number of tickets Taegan won from each game
    tickets_per_game = (total_value - 5) / (equal_tickets * ticket_value)

    result = tickets_per_game
    return result

print(solution())