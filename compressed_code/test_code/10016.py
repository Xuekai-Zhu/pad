def solution():
    
    marbles_at_start = 100
    marbles_per_game = 10
    games_played = 9
    marbles_won = marbles_at_start - 90
    games_lost = marbles_won // marbles_per_game
    result = games_lost
    return result

print(solution())