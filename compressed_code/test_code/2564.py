def solution():
    
    games_played = 200 + 100
    games_won = 0.63 * 200 + (100-43)
    win_percentage = games_won / games_played * 100
    result = win_percentage
    return result

print(solution())