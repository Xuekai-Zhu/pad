def solution():
    """Wade is the star player of the basketball team. His average points per game is 20, and his teammates' average points per game is 40. How many points will their team have in total after 5 games?"""
    wade_points_per_game = 20
    teammates_points_per_game = 40
    total_points_per_game = wade_points_per_game + teammates_points_per_game
    games_played = 5
    total_points = total_points_per_game * games_played
    result = total_points
    return result

print(solution())