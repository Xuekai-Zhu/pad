def solution():
    total_hits = 15 * 5  # total hits in the first 5 games
    best_player_hits = 25
    other_players_hits = total_hits - best_player_hits
    num_players = 11
    num_games = 6

    # Calculate the average hits per game for the other players
    avg_hits_per_game = other_players_hits / (num_players - 1) / 5

    # Calculate the total hits for the other players in the next 6 games
    total_other_player_hits = avg_hits_per_game * num_players * num_games

    # Calculate the average hits per player across the next 6 games
    avg_hits_per_player = (total_other_player_hits + best_player_hits) / num_players / (num_games + 5)
    result = avg_hits_per_player
    return result

print(solution())