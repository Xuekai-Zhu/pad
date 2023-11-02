def solution():
    games_played_mark = 10
    games_played_jill = 2 * games_played_mark
    games_won_mark = 1
    games_won_jill = .75 * games_played_jill
    total_games_won = games_won_mark + games_won_jill
    result = total_games_won
    return result

print(solution())