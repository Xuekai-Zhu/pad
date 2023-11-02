def solution():
    lefty_points = 20
    righty_points = lefty_points / 2
    other_teammate_points = righty_points * 6
    total_points = lefty_points + righty_points + other_teammate_points
    num_players = 3
    avg_points_per_player = total_points / num_players
    result = avg_points_per_player
    return result

print(solution())