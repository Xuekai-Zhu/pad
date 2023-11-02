def solution():
    # Calculate the number of games won out of the first 40
    games_won = 0.7 * 40

    # Calculate the total number of games the team will play
    total_games = 40 + 10

    # Calculate the number of games the team needs to win to achieve a 60% win rate
    games_needed_to_win = 0.6 * total_games

    # Calculate the number of games the team can afford to lose
    games_allowed_to_lose = games_needed_to_win - games_won

    result = games_allowed_to_lose
    return result

print(solution())