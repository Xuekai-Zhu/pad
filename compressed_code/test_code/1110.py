def solution():
    
    total_games = 20
    wins = 14
    losses = 2
    draws = total_games - wins - losses
    win_points = 3
    draw_points = 1
    total_points = (wins * win_points) + (draws * draw_points)
    result = total_points
    return result

print(solution())