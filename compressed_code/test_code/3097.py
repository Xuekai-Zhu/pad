def solution():
    
    lefty_points = 20
    righty_points = lefty_points / 2
    other_teammate_points = 6 * righty_points
    total_team_points = lefty_points + righty_points + other_teammate_points
    avg_points_per_player = total_team_points / 3
    result = avg_points_per_player
    return result

print(solution())