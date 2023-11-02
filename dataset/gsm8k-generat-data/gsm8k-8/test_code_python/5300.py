def solution():
    # Calculate the total number of hits in the first 20 games
    total_hits = 20 * 2

    # Calculate the total number of games for the whole season
    total_games = 20 + 10

    # Calculate the total number of hits needed to average 3 hits per game for the whole season
    total_hits_needed = total_games * 3

    # Calculate the number of hits needed in the remaining 10 games
    hits_needed = total_hits_needed - total_hits

    # Calculate the average number of hits needed in the remaining 10 games
    average_hits_needed = hits_needed / 10
    result = average_hits_needed
    return result

print(solution())