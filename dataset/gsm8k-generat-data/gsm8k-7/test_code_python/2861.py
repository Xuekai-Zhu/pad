def solution():
    total_games = 30 # 20 games played and 10 games left
    desired_wins = total_games*(2/3) # 2/3 of games must be won to make playoffs
    current_wins = 12 # number of games won so far
    games_left = 10 # number of games left
    remaining_wins = desired_wins - current_wins
    remaining_games = total_games - 20 # number of games left to be played
    remaining_win_percentage = remaining_wins / remaining_games # find win percentage needed for remaining games
    remaining_wins_needed = remaining_win_percentage * games_left # multiply win percentage by remaining games to find remaining wins needed
    result = round(remaining_wins_needed) # round answer to nearest integer
    return result

print(solution())