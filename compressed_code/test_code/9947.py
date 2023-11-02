def solution():
    
    games_played = 20
    hits_so_far = games_played * 2
    remaining_games = 10
    total_hits_goal = (games_played + remaining_games) * 3
    hits_needed = total_hits_goal - hits_so_far
    average_hits_needed = hits_needed / remaining_games
    result = average_hits_needed
    
    return result

print(solution())