def solution():
    """Lefty scores 20 points in a game and his teammate Righty scores half as many as Lefty does. Their other teammate scores 6 times as much as Righty does. What are the average points scored per player on the team?"""
    lefty_points = 20
    righty_points = lefty_points / 2
    other_teammate_points = 6 * righty_points
    total_team_points = lefty_points + righty_points + other_teammate_points
    avg_points_per_player = total_team_points / 3
    result = avg_points_per_player
    return result

print(solution())