def solution():
    # Calculate the total number of hits the team made in first 5 games
    total_hits = 15 * 5

    # Calculate the total number of hits made by all the players except the best player
    other_players_hits = total_hits - 25

    # Calculate the average number of hits per player over the next 6 games
    average_hits_per_player = other_players_hits / (11 * 6)

    result = average_hits_per_player
    return result

print(solution())