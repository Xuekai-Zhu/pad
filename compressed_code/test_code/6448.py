def solution():
    
    points_per_win = 10
    total_points = 60
    lost_points = 20
    rounds_played = (total_points + lost_points) / points_per_win
    result = rounds_played
    return result

print(solution())