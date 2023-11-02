def solution():
    # Define the variables
    mark_games_played = 10
    mark_games_won = 1
    jill_games_played = 2 * mark_games_played
    jill_games_won = 0.75 * jill_games_played

    # Calculate total games played and won
    total_games_played = mark_games_played + jill_games_played
    total_games_won = mark_games_won + jill_games_won

    # Calculate the number of games Jenny won
    jenny_wins = total_games_won - mark_games_won

    result = jenny_wins
    return result

print(solution())