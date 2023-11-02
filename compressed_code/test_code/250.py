def solution():
    
    game_time = 90
    mark_played1 = 20
    mark_played2 = 35
    total_played = mark_played1 + mark_played2
    time_on_sideline = game_time - total_played
    result = time_on_sideline
    return result

print(solution())