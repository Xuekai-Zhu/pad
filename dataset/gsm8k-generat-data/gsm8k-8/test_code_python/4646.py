def solution():
    # Define the current and target passing yards
    current_yards = 4200
    target_yards = 5999

    # Calculate the remaining yards needed to beat the record
    remaining_yards = target_yards - current_yards

    # Calculate the number of games left
    games_left = 6

    # Calculate the average passing yards per game needed to beat the record
    yards_per_game = remaining_yards / games_left
    result = yards_per_game
    return result

print(solution())