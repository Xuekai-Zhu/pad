def solution():
    # Calculate the number of games won
    games_won = round(0.7 * 40)  # 70% of 40 games
    games_left = 10  # 10 games left to play
    total_games = 40 + games_left  # total number of games played
    games_needed_to_win = round(0.6 * total_games)  # 60% of total games needed to be won
    games_can_lose = games_needed_to_win - games_won  # number of games the team can afford to lose and still win 60% of games
    result = games_can_lose
    return result

print(solution())