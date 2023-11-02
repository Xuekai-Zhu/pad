def solution():
    total_hits = 20 * 2 # total hits in first 20 games
    remaining_games = 10
    remaining_hits_needed = (remaining_games * 3) - total_hits # hits needed to average 3 for the season
    hits_per_game_needed = remaining_hits_needed / remaining_games
    result = hits_per_game_needed
    return result

print(solution())