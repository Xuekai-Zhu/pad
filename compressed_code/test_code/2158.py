def solution():
    
    play_time = 120 
    point_time = 5 
    total_points = play_time // point_time
    games_won = total_points // 8
    result = games_won
    return result

print(solution())