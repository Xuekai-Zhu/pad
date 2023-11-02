def solution():
    passing_tds_record = 89
    games_played = 14
    passing_tds = passing_tds_record - games_played
    passing_tds_needed = 2
    tds_per_game_needed = passing_tds / passing_tds_needed
    result = tds_per_game_needed
    return result

print(solution())