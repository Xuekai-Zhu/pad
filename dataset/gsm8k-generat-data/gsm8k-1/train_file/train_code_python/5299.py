def solution():
    """Javier plays 2 baseball games a week. In each of his first 20 games, he averaged 2 hits. If he has 10 games left, how many hits a game does he have to average to bring his average for the season up to 3 hits a game?"""
    games_played = 20
    hits_so_far = games_played * 2
    remaining_games = 10
    total_hits_goal = (games_played + remaining_games) * 3
    hits_needed = total_hits_goal - hits_so_far
    average_hits_needed = hits_needed / remaining_games
    result = average_hits_needed
    
    return result

print(solution())