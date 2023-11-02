def solution():
    """Team Soccer Stars plays in a soccer league. They played a total of 20 games, and won 14 games, lost 2, and drew the rest of the matches. They earn 3 points for a win, 1 point for a draw, and nothing for a loss. How many points did they have at the end of the season?"""
    total_games = 20
    wins = 14
    losses = 2
    draws = total_games - wins - losses
    win_points = 3
    draw_points = 1
    total_points = (wins * win_points) + (draws * draw_points)
    result = total_points
    return result

print(solution())