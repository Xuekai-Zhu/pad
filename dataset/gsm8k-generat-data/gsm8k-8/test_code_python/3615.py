def solution():
    # Calculate the total number of hits the team had in the first 5 games
    total_hits = 15 * 5

    # Calculate the number of hits the best player had in the first 5 games
    best_player_hits = 25

    # Calculate the number of hits by the other players in the first 5 games
    other_players_hits = total_hits - best_player_hits

    # Calculate the average hits by the other players in the first 5 games
    avg_other_players = other_players_hits / (11 - 1)

    # Calculate the total hits by the other players in the next 6 games
    total_other_players_hits = avg_other_players * 6

    # Calculate the average hits by each player across the next 6 games
    avg_hits_per_player = (total_other_players_hits + best_player_hits) / 11

    result = avg_hits_per_player
    return result

print(solution())