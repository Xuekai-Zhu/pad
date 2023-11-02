def solution():
    """Lefty scores 20 points in a game and his teammate Righty scores half as many as Lefty does. Their other teammate scores 6 times as much as Righty does. What are the average points scored per player on the team?"""
    lefty_score = 20
    righty_score = lefty_score / 2
    third_teammate_score = righty_score * 6
    total_points = lefty_score + righty_score + third_teammate_score
    num_players = 3
    average_score = total_points / num_players
    result = average_score
    return result

print(solution())