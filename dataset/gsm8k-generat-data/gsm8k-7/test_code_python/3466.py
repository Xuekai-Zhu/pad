def solution():
    total_points = 720
    num_games = 24

    # Calculate the average number of points per game in the previous 24 games
    avg_points_per_game = total_points / num_games

    # Calculate half of the average points per game
    half_avg_points = avg_points_per_game / 2

    # Calculate the opponent's total points in the championship game
    opp_total_points = 2 * (half_avg_points - 2) * num_games

    # Add the opponent's points to UF's total points to get the total points scored in the championship game
    total_champ_points = total_points + opp_total_points

    # Calculate the opponent's points by subtracting UF's total points from the total championship points
    opp_points = total_champ_points - total_points
    result = opp_points
    return result

print(solution())