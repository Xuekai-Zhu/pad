def solution():
    hits_per_game = 15  # The team has averaged 15 hits per game over their first 5 games
    num_players = 11  # There are 11 players on the team
    total_hits = hits_per_game * 5 + 25  # The best player has 25 total hits, and the team has played 5 games
    remaining_games = 6  # The team has 6 games left to play

    # Calculate the average hits per player across the remaining games
    average_hits_per_player = (total_hits / num_players) / 11

    # Calculate the total hits each player will have across the remaining games
    total_hits_each_player = average_hits_per_player * remaining_games
    result = total_hits_each_player
    return result

print(solution())