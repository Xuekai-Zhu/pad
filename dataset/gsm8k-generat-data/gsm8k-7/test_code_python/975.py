def solution():
    free_throw_percentage = 0.70
    fouls_per_game = 5
    shots_per_foul = 2
    games_played = 20
    games_played_percentage = 0.80
    
    # Calculate the total number of fouls John gets over all the games he plays
    total_fouls = games_played * fouls_per_game * games_played_percentage

    # Calculate the total number of free throws John gets
    total_free_throws = total_fouls * shots_per_foul * free_throw_percentage

    result = total_free_throws
    return result

print(solution())