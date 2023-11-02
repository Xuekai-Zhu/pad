def solution():
    # Calculate the number of games Bill has won in the first 200 games
    games_won = 0.63 * 200

    # Calculate the total number of games Bill will have played after 100 more games
    total_games = 200 + 100

    # Calculate how many games Bill needs to lose to have a total of 43 losses
    games_lost = 43 - (total_games - 200 - games_won)

    # Calculate the number of games Bill will have won after the 100 more games
    new_games_won = games_won + (100 - games_lost)

    # Calculate Bill's new win percentage
    new_win_percentage = new_games_won / total_games
    result = new_win_percentage
    return result

print(solution())