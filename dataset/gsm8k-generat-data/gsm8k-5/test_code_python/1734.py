def solution():
    wade_points_per_game = 20
    teammates_points_per_game = 40
    total_points_per_game = wade_points_per_game + teammates_points_per_game
    games = 5

    # Calculate the total points scored by the team in 5 games
    total_points = total_points_per_game * games
    result = total_points
    return result

print(solution())