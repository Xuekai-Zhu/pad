def solution():
    # Calculate the number of games won by Bill in the first 200 games
    games_won_1 = 0.63 * 200

    # Calculate the number of games lost by Bill in the first 200 games
    games_lost_1 = 200 - games_won_1

    # Calculate the total number of games played by Bill after playing 100 more games
    total_games = 200 + 100

    # Calculate the number of games lost by Bill after playing 100 more games
    games_lost_2 = 43

    # Calculate the total number of games won by Bill
    total_games_won = games_won_1 + (total_games - 200 - 43)

    # Calculate the new win percentage
    new_win_percentage = total_games_won / total_games
    result = new_win_percentage
    return result

print(solution())