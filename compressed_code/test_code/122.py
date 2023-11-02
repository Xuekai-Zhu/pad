def solution():
    
    touchdowns_per_game = 4
    touchdown_points = 6
    conversion_points = 2
    total_games = 15
    total_touchdowns = touchdowns_per_game * total_games
    total_conversion_points = conversion_points * 6
    total_points = (total_touchdowns * touchdown_points) + total_conversion_points
    old_record = 300
    points_above_record = total_points - old_record
    result = points_above_record
    return result

print(solution())