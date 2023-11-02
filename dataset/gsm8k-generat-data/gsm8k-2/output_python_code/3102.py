def solution():
    """Taegan goes to a carnival where she wins tickets from each of the 5 carnival games and also finds 5 tickets on the floor. Each ticket is worth $3. In total, she has tickets that total a value of $30. If Taegan won an equal number of tickets from each of the games, how many tickets did she win from each game?"""
    total_tickets = 5 + 5
    total_value = 30
    ticket_value = 3
    game_tickets = total_tickets // 5
    game_value = game_tickets * ticket_value
    found_tickets = total_tickets - game_tickets * 5
    found_value = found_tickets * ticket_value
    needed_value = total_value - found_value
    game_tickets_needed = needed_value // game_value
    result = game_tickets_needed
    return result

print(solution())