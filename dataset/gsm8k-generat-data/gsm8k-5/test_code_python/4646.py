def solution():
    current_yards = 4200  # Tom Brady currently has 4200 yards
    remaining_games = 6  # There are 6 games left in the season
    record_yards = 5999  # The passing yards record for a season is 5999 yards

    # Calculate the number of yards Tom Brady needs to pass the record
    needed_yards = record_yards - current_yards

    # Calculate the average number of passing yards per game needed to beat the record
    average_yards_per_game = needed_yards / remaining_games
    result = average_yards_per_game
    return result

print(solution())