def solution():
    wade_points_per_game = 20
    teammates_points_per_game = 40
    num_games = 5

    # Calculate the total points that Wade will score in 5 games
    wade_total_points = wade_points_per_game * num_games

    # Calculate the total points that Wade's teammates will score in 5 games
    teammates_total_points = teammates_points_per_game * num_games

    # Calculate the total points the team will have in 5 games
    total_points = wade_total_points + teammates_total_points
    result = total_points
    return result

print(solution())