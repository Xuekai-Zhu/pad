def solution():
    games_played = 100
    games_tied = 40
    money_lost = 30
    games_won = games_played - games_tied - money_lost
    result = games_won
    return result

print(solution())