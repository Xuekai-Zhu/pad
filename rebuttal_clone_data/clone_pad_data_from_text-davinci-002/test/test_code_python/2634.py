def solution():
    passing_yards_record = 5999
    tom_brady_yards = 4200
    games_left = 6
    yards_needed = passing_yards_record - tom_brady_yards
    yards_per_game_needed = yards_needed / games_left
    result = yards_per_game_needed
    return result

print(solution())