def solution():
    """Tom Brady is shy of the passing yards record in a season. The current record is 5999 yards. He currently has 4200 yards with 6 games left in the season. How many passing yards per game does he need to average to beat the record?"""
    # Define the current passing yards, remaining games, and the passing yards record
    current_yards = 4200
    remaining_games = 6
    record_yards = 5999

    # Calculate the total passing yards needed to break the record
    total_yards_needed = record_yards - current_yards

    # Calculate the average passing yards per game needed to break the record
    yards_per_game_needed = total_yards_needed / remaining_games

    # return the result
    result = yards_per_game_needed
    return result

print(solution())