def solution():
    # Calculate the number of hits Javier has so far
    hits_so_far = 20 * 2  # He averaged 2 hits in each of his first 20 games

    # Calculate the number of hits he needs in the remaining 10 games
    hits_remaining = 10 * 3  # He wants to average 3 hits per game in the entire season, so he needs 3 hits in each of the remaining 10 games

    # Calculate the total number of games in the season
    total_games = 20 + 10

    # Calculate the total number of hits he needs to average 3 hits a game in the entire season
    total_hits_needed = total_games * 3

    # Calculate the number of hits he needs in the remaining 10 games to bring his average up to 3 hits a game
    hits_needed = total_hits_needed - hits_so_far - hits_remaining

    # Calculate the average number of hits he needs to achieve in the remaining 10 games
    average_hits_needed = hits_needed / 10
    result = average_hits_needed
    return result

print(solution())