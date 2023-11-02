def solution():
    
    total_points = 270
    total_players = 9
    avg_points_5 = 50
    total_points_5 = avg_points_5 * 5
    total_points_remainder = total_points - total_points_5
    total_players_remainder = total_players - 5
    avg_points_remainder = total_points_remainder / total_players_remainder
    result = avg_points_remainder
    return result

print(solution())