def solution():
    """Tom Brady is shy of the passing yards record in a season. The current record is 5999 yards. He currently has 4200 yards with 6 games left in the season. How many passing yards per game does he need to average to beat the record?"""
    current_yards = 4200
    record_yards = 5999
    remaining_games = 6
    yards_needed = record_yards - current_yards
    yards_per_game_needed = yards_needed / remaining_games
    result = yards_per_game_needed
    return result

print(solution())