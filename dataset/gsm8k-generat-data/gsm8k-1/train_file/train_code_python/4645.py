def solution():
    """Tom Brady is shy of the passing yards record in a season. The current record is 5999 yards. He currently has 4200 yards with 6 games left in the season. How many passing yards per game does he need to average to beat the record?"""
    current_yards = 4200
    games_left = 6
    yards_needed = 5999 - current_yards
    yards_per_game = yards_needed / games_left
    result = yards_per_game
    return result

print(solution())