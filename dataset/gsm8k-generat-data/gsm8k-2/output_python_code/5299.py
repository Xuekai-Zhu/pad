def solution():
    """Javier plays 2 baseball games a week. In each of his first 20 games, he averaged 2 hits. If he has 10 games left, how many hits a game does he have to average to bring his average for the season up to 3 hits a game?"""
    total_games = 30
    total_hits_so_far = 20 * 2
    remaining_games = 10
    remaining_hits_needed = (total_hits_so_far + (remaining_games * 3)) - (total_games * 3)
    hits_per_game_needed = remaining_hits_needed / remaining_games
    result = hits_per_game_needed
    return result

print(solution())