def solution():
    """Tom Brady is shy of the passing yards record in a season. The current record is 5999 yards. He currently has 4200 yards with 6 games left in the season. How many passing yards per game does he need to average to beat the record?"""
    # Define the current passing yards and the number of remaining games
    current_yards = 4200
    remaining_games = 6

    # Define the record passing yards
    record_yards = 5999

    # Calculate the number of passing yards Brady needs to average per game to beat the record
    yards_per_game = (record_yards - current_yards) / remaining_games

    # Display the yards per game needed
    result = yards_per_game
    return result

print(solution())