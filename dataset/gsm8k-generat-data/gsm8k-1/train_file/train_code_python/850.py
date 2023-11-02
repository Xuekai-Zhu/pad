def solution():
    """In a card game, you are awarded 10 points if you win one round. While playing, Jane ends up with 60 points. If she lost 20 points, then how many rounds did she play?"""
    points_per_win = 10
    total_points = 60
    lost_points = 20
    rounds_played = (total_points + lost_points) / points_per_win
    result = rounds_played
    return result

print(solution())