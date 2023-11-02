def solution():
    # Calculate the total number of hits in the first 20 games
    total_hits = 20 * 2  # Javier averages 2 hits per game in the first 20 games

    # Calculate the total number of hits needed for the entire season
    total_hits_needed = (20 + 10) * 3  # Javier wants to average 3 hits per game for the entire season, and has 10 games left.

    # Calculate the number of hits that Javier needs to get in the remaining 10 games
    hits_needed = total_hits_needed - total_hits

    # Calculate the average number of hits that Javier needs to get in each of the remaining games
    average_hits_needed = hits_needed / 10

    result = average_hits_needed
    return result

print(solution())