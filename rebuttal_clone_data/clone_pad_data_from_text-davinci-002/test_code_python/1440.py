def solution():
    games_played = 20
    games_won = 14
    games_lost = 2
    games_drawn = games_played - games_won - games_lost
    points_for_win = 3
    points_for_draw = 1
    total_points = (games_won * points_for_win) + (games_drawn * points_for_draw)
    result = total_points
    return result

print(solution())