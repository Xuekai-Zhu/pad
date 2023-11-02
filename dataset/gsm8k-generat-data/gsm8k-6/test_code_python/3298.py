def solution():
    # Calculate the number of games won by Bill
    games_won = 0.63 * 200  # 63% of 200 games

    # Calculate the total number of games played by Bill
    total_games = 200 + 100  # 200 initial games + 100 more games

    # Calculate the new number of games won by Bill after losing 43 games
    new_games_won = games_won + (100 - 43)  # 100 games - 43 losses

    # Calculate the new win percentage of Bill
    new_win_percentage = (new_games_won / total_games) * 100

    result = new_win_percentage
    return result

print(solution())