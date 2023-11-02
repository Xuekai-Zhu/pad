def solution():
    points_per_win = 10
    total_points = 60
    points_lost = 20
    rounds_played = (total_points + points_lost) / points_per_win
    result = rounds_played
    return result

print(solution())