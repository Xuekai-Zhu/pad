def solution():
    
    total_games = 20
    wins = 14
    losses = 2
    draws = total_games - wins - losses
    win_points = wins * 3
    draw_points = draws * 1
    total_points = win_points + draw_points
    result = total_points
    return result

print(solution())