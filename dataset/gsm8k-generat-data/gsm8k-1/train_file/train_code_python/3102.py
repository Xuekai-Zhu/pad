def solution():
    """Taegan goes to a carnival where she wins tickets from each of the 5 carnival games and also finds 5 tickets on the floor. Each ticket is worth $3. In total, she has tickets that total a value of $30. If Taegan won an equal number of tickets from each of the games, how many tickets did she win from each game?"""
    total_tickets = 5 + 5  # from games and found
    ticket_value = 3
    total_value = 30
    tickets_per_game = total_tickets / 5
    tickets_won = total_value / ticket_value
    tickets_per_game_won = tickets_won / 5
    result = tickets_per_game_won
    return result

print(solution())